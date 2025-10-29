# coding: utf-8
'''
INSERT

Inserts an entire row or upserts data into an existing row; statement must include the full Primary_key. Requires a value for each component of the primary key, but not for any other columns. Missing columns are unset by default and do not create tombstones in the database. Returns no results unless IF NOT EXISTS is used.

**Restriction:**

-   Insert does not support counter columns, use UPDATE instead.
-   A PRIMARY KEY consists of a the partition key followed by the clustering columns.

Synopsis


INSERT [ JSON ] INTO [keyspace_name.]table_name
  [ column_list VALUES column_values ] 
  [ IF NOT EXISTS ] 
  [ USING [ TTL seconds ] [ [ AND ] TIMESTAMP epoch_in_microseconds ] ] ;


**Note:** INSERT also supports JSON syntax to provide manual testing and troubleshooting from the command line, see Inserting JSON formatted values.

**Note:** To modify a base table that has a materialized view (MV) using an `INSERT` or `UPDATE` command if access permissions are enabled, a user must be granted `MODIFY` or `ALL PERMISSIONS` on the base table.

column_list
    Comma-separated list of columns. All PRIMARY KEY fields are required. Nulls are inserted into any static columns that are excluded.

column_values
    For each column, enter the corresponding list of values. Use the same order as the column_list.

    Enter data using a literal or the following syntax for collections:

    -   Set: Enter values between curly braces: `{ literal [, ...] }`.
    -   List: Enter values between square brackets: `[literal [, ...]]`.
    -   Map: Enter values between curly braces: `{ key : value [, ...] }`.

TTL seconds
    Set TTL in seconds. After TTL expires, inserted data is automatically marked as deleted (with a tombstone). The TTL settings applies only to the inserted data, not the entire column. Any subsequent updates to the column resets the TTL. By default, values never expire.

    You can set a default TTL for an entire table by setting the table's default_time_to_live property. Setting TTL on a column using the INSERT or UPDATE command overrides the table TTL.

    **Warning:** The database storage engine can only encode TTL timestamps through `January 19 2038 03:14:07 UTC` due to the Year 2038 problem. The TTL date overflow policy determines whether requests with expiration timestamps later than the maximum date are rejected or inserted. See -Dcassandra.expiration_date_overflow_policy.

IF NOT EXISTS
    Inserts a new row of data if no rows match the PRIMARY KEY values.

TIMESTAMP epoch_in_microseconds
    Marks inserted data (write time) with `TIMESTAMP`. Enter the time since epoch (January 1, 1970) in microseconds. By default, the actual time of write is used.

    **Restriction:** INSERT does not support IF NOT EXISTS and USING TIMESTAMP in the same statement.


'''
