# coding: utf-8
'''
CREATE FUNCTION

Executes user-provided Java or Javascript code in SELECT, UPDATE, INSERT or provides a building block for user-defined aggregate. Functions are only available in the keyspace where they were created.

UDF supports Java generic methods or Javascript in the user provided codeblock. UDFs are susceptible to all of the normal issues that may occur with the chosen programming language. Safe guard against exceptions, such as null pointer exceptions, illegal arguments, or any other potential sources of problems. An exception during function execution results in the entire statement failing.

**Note:** By default, the database does not allow UDFs. To enable, change the following settings in the cassandra.yaml and restart all nodes:

-   Set enable_user_defined_functions to `true` - allow users to create custom functions. Only Java is allowed in codeblocks if enable_scripted_user_defined_functions is `false`.
-   (Optional ) Set enable_scripted_user_defined_functions to `true` - allow function codeblocks to use Javascript.
-   (Optional) Set enable_user_defined_functions_threads to false to allow functions in GROUP BY clauses.

Synopsis


CREATE [ OR REPLACE ] FUNCTION [ IF NOT EXISTS ] [keyspace_name.]function_name (argument_list [ , ... ])
  ( CALLED | RETURNS NULL ) ON NULL INPUT RETURNS type 
  [ DETERMINISTIC ]
  [ MONOTONIC [ ON argument_name ] ]
  LANGUAGE ( java | javascript ) AS $$ code_block $$ ;


function_name
    Specify a keyspace-qualified function name. Names must start with a letter or number. To preserve case, enclose the name in double-quotes.

OR REPLACE
    Overwrite the function, if one already exists with the same name.

    **Note:** Cannot be used with the `IF NOT EXISTS` option.

IF NOT EXISTS
    Performs no operation and suppresses the error message if a function with the same name already exists.

argument_list
    Comma separated list of arguments with data types passed to the code block for processing:

    
    arg_name cql_type [,...]
    

    In the list, specify an argument name followed by the CQL data type.

    For requests, an argument value can be read from a column with the corresponding data type or manually entered (literal).

CALLED ON NULL INPUT
    Executes the user-provided code block even if the input value is null or missing.

RETURNS NULL ON NULL INPUT
    Does not execute the user-provided code block on null values; returns null.

RETURNS cql_data_type
    Map the expected output from the code block to a compatible CQL data type.

DETERMINISTIC
    Specify for functions that always returns the same output for a certain input. For example, toJson() is a deterministic function, while now() and currentDate() are not.

    Default: `false` (non-deterministic).

    **Note:** GROUP BY only supports functions that are both deterministic and monotonic.

MONOTONIC [ ON argument_name ]
    All arguments or the specified argument are monotonic if they are either entirely non-increasing or non-decreasing.

    **Note:** GROUP BY only supports functions that are both deterministic and monotonic.

LANGUAGE language_name
    Supported types are `java` or `javascript`.

    **Tip:** When enable_scripted_user_defined_functions is false and enable_user_defined_functions is true, Java is the only supported language.

'code_block' | $$ code_block $$
    Enclose the code block in single quotes or if the code block contains any special characters enclose it in double dollar signs ($$). The code is wrapped as a function and applied to the target variables.


'''
