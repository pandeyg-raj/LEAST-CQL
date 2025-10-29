# coding: utf-8
'''
ALTER MATERIALIZED VIEW

Changes materialized view table properties. The statement returns no results.

**Restriction:**

-   Changing columns is not supported.
-   Change log, CDC, is not available for materialized views.

Synopsis


ALTER MATERIALIZED VIEW [keyspace_name.]view_name 
  WITH table_options [ AND table_options ... ] ;


keyspace_name
    Selects a keyspace.

view_name
    Selects the materialized view.

table_options
    Table options are defined when the materialized view is created. Modify the table_options in the WITH clause using the following syntax:

    -   Single value using the `option_name = 'value'`. Enclose string values in single quotes, and no quotes for numbers, boolean, etc.
    -   Specify options with multiple subproperties in simple JSON format, option_name = { option_map }.
    -   Set multiple table options using AND.


'''
