# coding: utf-8
'''
CREATE AGGREGATE

Defines a user-defined aggregate. An aggregate executes a user-define function (UDF) on each row in a selected data set, optionally runs a final UDF on the result set and returns a single value, for example average or standard deviation.

Synopsis


CREATE [ OR REPLACE ] AGGREGATE [ IF NOT EXISTS ] 
  [keyspace_name.]aggregate_name (cql_type)
  SFUNC udf_name 
  STYPE cql_type
  FINALFUNC udf_name 
  INITCOND init_value
  [ DETERMINISTIC ] ;


OR REPLACE
    Overwrites existing aggregate (with the same name). When OR REPLACE is not specified the operations fails if an aggregate with the same name already exists.

IF NOT EXISTS
    Creates an aggregate if it does not already exist, and displays no error if it does exist.

    **Note:** IF NOT EXISTS and OR REPLACE are not supported in the same statement.

cql_type
    Specify the CQL type input.

    **Restriction:** Frozen collections are not supported.

SFUNC udf_name
    Specify a user-defined function. Calls the state function (SFUNC) for each row. The first parameter declared in the user-defined function is the *state* parameter; the function's return value is assigned to the state parameter, which is passed to the next call. Pass multiple values using collection types, such as tuples.

STYPE cql_type
    CQL type of the parameter returned by the state function.

FINALFUNC udf_name
    User-defined function executed on the final values in the state parameter.

INITCOND [init_value]
    Define the initial condition, values, of the first parameter in the SFUNC. Set to null when no value defined.

DETERMINISTIC
    Always returns the same output for a certain input. Requires an initial condition and returns a single value.

    Default: `false` (non-deterministic).

    **Note:** GROUP BY only supports aggregates that are deterministic.


'''
