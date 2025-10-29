# coding: utf-8
'''
CREATE MATERIALIZED VIEW

Optimizes read requests by allowing different partitioning and clustering columns than the base table and eliminates the need for individual write requests to multiple tables. When data is written to the base table, it is also automatically written to all associated materialized views.

**Restriction:**

-   Use all base table primary keys in the materialized view.
-   Multiple non-primary key columns from the base table are supported when the partition key is the same as in the base table, otherwise only a single non-primary key from the base table is allowed in the materialized view's PRIMARY KEY.
-   Static columns are not supported.

Synopsis


CREATE MATERIALIZED VIEW [ IF NOT EXISTS ] [keyspace_name.]view_name
  AS SELECT [ (column_list) ]
  FROM [keyspace_name.]table_name
  [ WHERE column_name IS NOT NULL
  [ AND column_name IS NOT NULL ... ] ]
  [ AND relation [ AND ... ] ] 
  PRIMARY KEY ( column_list )
  [ WITH [ table_properties ]
  [ [ AND ] CLUSTERING ORDER BY (cluster_column_name order_option) ] ] ;


IF NOT EXISTS
    Optional. Suppresses the error message when attempting to create a materialized view that already exists. Use to continue executing commands, such as a `SOURCE` command. The option only validates that a materialized view with the same name exists; columns, primary keys, properties, and other settings can differ.

keyspace_name
    Optional. When no keyspace is selected or to create the view in another keyspace, set the keyspace name before the materialized view name.

    **Note:** Base tables and materialized views are always in the same keyspace.

view_name
    Materialized view names can only contain alpha-numeric characters and underscores. The view name must begin with a number or letter and can be up to 49 characters long.

column_list
    Comma-separated list of columns from the base table to include in the materialized view.

    Static columns, even when specified, are not supported and not included in the materialized view.

column_name IS NOT NULL
    Test all columns for null values in the `WHERE` clause. Separate each condition with `AND`. Rows with null values in any column are not inserted into the materialized view table.

AND relation
    Other relations that target the specific data needed.

PRIMARY KEY ( column_list )
    Comma-separated list of columns used to partition and cluster the data. You can add non-primary key columns from the base table. Reorder the primary keys as needed to query the table more efficiently, including changing the partitioning and clustering keys.

table_properties
    Optional. Specify table properties if different than default. Separate table property definitions with an AND. See table properties.

    **Note:** The base table properties are not copied.

    **Restriction:** Change log, CDC, is not available for materialized views. Not all table properties are available when creating a materialized view; for example, `default_time_to_live` is not available.


'''
