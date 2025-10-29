# coding: utf-8
'''
DELETE

Removes data from one or more selected columns (data is replaced with null) or removes the entire row when no column is specified. Deletes data in each selected partition atomically and in isolation. Data is not removed from disk immediately; it is marked with a tombstone and then removed after the grace period.

CAUTION:

Using `DELETE` can impact performance. Tombstones are created, causing stale data to be read until removed by a compaction.

Synopsis


DELETE [ column_name [ term ] [ , ... ] ]
  FROM [keyspace_name.]table_name 
  [ USING TIMESTAMP timestamp_value ]
  WHERE PK_column_conditions 
  [ ( IF EXISTS | IF static_column_conditions ) ] ;


column_name
    Set column to delete or use a comma-separated list of columns. When no column is specified, the entire row is deleted.

term
    Element identifier for collection types:

    -   Lists specify the index number of the item, where 0 is the first.
    -   Maps specify the element key of the item.

timestamp_value
    Deletes values older than the timestamp_value.

PK_column_conditions
    Syntax to match PRIMARY KEY values. Separate multiple conditions with AND.

    **Restriction:**

    -   Only equals (=) or IN are supported.
    -   Ranges (IN) are not supported when specifying a static column condition; see IF condition.
    -   When removing data from columns in matching rows, you must specify a condition for all primary keys.

IF EXISTS
    Error when the statement results in no operation.

IF condition
    Specify conditions for static fields to match. Separate multiple conditions with AND.

    **Restriction:** Modifies the primary key statement, all primary keys required.


'''
