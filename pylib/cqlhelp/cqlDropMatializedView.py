# coding: utf-8
'''
DROP MATERIALIZED VIEW

Immediate, irreversible removal of a materialized view, including all data it contains. This operation has no effect on the base table.

**Restriction:** Drop all materialized views associated with a base table before dropping the table.

Synopsis


DROP MATERIALIZED VIEW [ IF EXISTS ] [keyspace_name.]view_name ;


IF EXISTS
    If the materialized view does not exist, the operation fails without an error. Optional.

keyspace_name
    To drop a materialized view in a keyspace other than the current keyspace, put the keyspace name in front of the materialized view name, followed by a period.

view_name
    The name of the materialized view to drop.


'''
