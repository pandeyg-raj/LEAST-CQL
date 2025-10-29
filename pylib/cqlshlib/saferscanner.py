# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# SaferScanner is just like re.Scanner, but it neuters any grouping in the lexicon
# regular expressions and throws an error on group references, named groups, or
# regex in-pattern flags. Any of those can break correct operation of Scanner.

import re

try:
    # before python 3.11
    from sre_constants import BRANCH, SUBPATTERN, GROUPREF, GROUPREF_IGNORE, GROUPREF_EXISTS
    from re import sre_compile as sre_compile
    from re import sre_parse as sre_parse
except ImportError:
    # since python 3.11, CASSANDRA-18088
    from re._constants import BRANCH, SUBPATTERN, GROUPREF, GROUPREF_IGNORE, GROUPREF_EXISTS
    from re import _compiler as sre_compile
    from re import _parser as sre_parse

from sys import version_info


class SaferScannerBase(re.Scanner):

    @classmethod
    def subpat(cls, phrase, flags):
        return cls.scrub_sub(sre_parse.parse(phrase, flags), flags)

    @classmethod
    def scrub_sub(cls, sub, flags):
        scrubbedsub = []
        seqtypes = (type(()), type([]))
        for op, arg in sub.data:
            if type(arg) in seqtypes:
                arg = [cls.scrub_sub(a, flags) if isinstance(a, sre_parse.SubPattern) else a
                       for a in arg]
            if op in (BRANCH, SUBPATTERN):
                arg = [None] + arg[1:]
            if op in (GROUPREF, GROUPREF_IGNORE, GROUPREF_EXISTS):
                raise ValueError("Group references not allowed in SaferScanner lexicon")
            scrubbedsub.append((op, arg))
        if sub.pattern.groupdict:
            raise ValueError("Named captures not allowed in SaferScanner lexicon")
        if sub.pattern.flags ^ flags:
            raise ValueError("RE flag setting not allowed in SaferScanner lexicon (%s)" % (bin(sub.pattern.flags),))
        return sre_parse.SubPattern(sub.pattern, scrubbedsub)


class Py2SaferScanner(SaferScannerBase):

    def __init__(self, lexicon, flags=0):
        self.lexicon = lexicon
        p = []
        s = sre_parse.Pattern()
        s.flags = flags
        for phrase, action in lexicon:
            p.append(sre_parse.SubPattern(s, [
                (SUBPATTERN, (len(p) + 1, self.subpat(phrase, flags))),
            ]))
        s.groups = len(p) + 1
        p = sre_parse.SubPattern(s, [(BRANCH, (None, p))])
        self.p = p
        self.scanner = sre_compile.compile(p)


class Py36SaferScanner(SaferScannerBase):

    def __init__(self, lexicon, flags=0):
        self.lexicon = lexicon
        p = []
        s = sre_parse.Pattern()
        s.flags = flags
        for phrase, action in lexicon:
            gid = s.opengroup()
            p.append(sre_parse.SubPattern(s, [(SUBPATTERN, (gid, 0, 0, sre_parse.parse(phrase, flags))), ]))
            s.closegroup(gid, p[-1])
        p = sre_parse.SubPattern(s, [(BRANCH, (None, p))])
        self.p = p
        self.scanner = sre_compile.compile(p)


class Py38SaferScanner(SaferScannerBase):

    def __init__(self, lexicon, flags=0):
        self.lexicon = lexicon
        p = []
        s = sre_parse.State()
        s.flags = flags
        for phrase, action in lexicon:
            gid = s.opengroup()
            p.append(sre_parse.SubPattern(s, [(SUBPATTERN, (gid, 0, 0, sre_parse.parse(phrase, flags))), ]))
            s.closegroup(gid, p[-1])
        p = sre_parse.SubPattern(s, [(BRANCH, (None, p))])
        self.p = p
        self.scanner = sre_compile.compile(p)


if version_info >= (3, 8):
    SaferScanner = Py38SaferScanner
elif version_info.major == 3:
    SaferScanner = Py36SaferScanner
elif version_info.major == 2:
    SaferScanner = Py2SaferScanner
else:
    raise ValueError("Unrecognized python version " + version_info)
