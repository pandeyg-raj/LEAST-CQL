# coding: utf-8
'''
SELECT

Returns data from a single table. A `SELECT` statement without a `WHERE` clause is not recommended because all rows from all partitions are returned.

CAUTION:

DataStax recommends limiting queries to a single partition using the `WHERE` clause. Queries across multiple partitions can impact performance.

Synopsis


SELECT [ JSON ] selectors 
  FROM [keyspace_name.]table_name 
  [ WHERE [ primary_key_conditions ] [ AND ] [ index_conditions ]
  [ GROUP BY column_name [ , ... ] ]
  [ ORDER BY PK_column_name [ , ... ] ( ASC | DESC ) ] 
  [ ( LIMIT N | PER PARTITION LIMIT N ) ]
  [ ALLOW FILTERING ] ;


selectors
    Determines the columns returned in the results set.

    
    column_list | DISTINCT partition_key [ AS output_name ]
    

    **Restriction:** Use either a column list or `DISTINCT`partition_key.

column_list
    Determines the columns and column order returned in the result set. Specify a comma-separated list of columns or use an asterisk to return all columns in the stored order.

    
    column_name | function_name( argument_list )
    

    -   column_name: Includes a column in the result set.
    -   function_name( arguments ): Execute a function on the specified argument for each row in the result set. See CQL native functions and Creating a user-defined function (UDF).
    -   aggregate_name( arguments ): Executes the aggregate on matching data and returns a single result. See CQL native aggregates and CREATE AGGREGATE.

DISTINCT partition_key
    Returns unique values for the full partition key. Use a comma-separated list of columns for a composite partition key.

AS output_name
    Renames the column to the new output name in the result set; for example:

    
    COUNT(id) AS "Cyclist Count"
    

    **Note:** If the name contains special characters, spaces, or to retain capitalization, surround the new name with double quotes.

keyspace_name.table_name

The keyspace name is required to identify a table in a different keyspace or if no keyspace is set for the session. If the keyspace or table name contain uppercase letters, enclose the name in double quotation marks; for example:


FROM "TestTable"


primary_key_conditions

Improves the efficiency of the query using logic statements to identify the data location and allows filtering on the last clustering column.


partition_conditions
[ AND clustering_conditions ] | [ AND index_conditions ]


**Tip:** To return all the data stored on a partition specify just the partition key values.

Logical statement syntax

column_name
    Enclose column names that have uppercase or special characters in double quotes.

    **Note:** Enclose string values in single quotes.

operators
value
    Enclose string values in single quotes.

    **Note:** Enclose column names that have uppercase or special characters in double quotes.

Identifying the data location and filtering by clustering columns

Use `WHERE` clauses to maximize read efficiency by identifying the location of the data. The database evaluates the `WHERE` logical statements hierarchically:

1.  Partition key columns: Use the equals operator to identify all partition key values (or none). Ensure that the data model supports single partition queries to avoid performance issues.

    **Note:** Partitions are typically large sets of data. The partitioner distributes the data by creating a hash of the partition key columns and stores all the rows with the same hash on the same node. Similar or like data, such as partition key date column values 7/01/2017 and 7/02/2017, may not be located on the same node.

2.  Clustering columns determine the sort order within the partition. Data is sorted by the first clustering column, the second clustering column, and so on.

**Note:**`ALLOW FILTERING` overrides restrictions on filtering partition columns, clustering columns, and regular columns, but can negatively impact performance, causing read latencies. Avoid `ALLOW FILTERING` in a production environment. In test environments, use cqlsh TRACING to analyze performance problems.

partition_conditions
    The database requires that all partitions are restricted except when querying a secondary or search index. Use logic statements that identify the partition key columns with these operators:

    -   **Equals (=)**: Any partition key column.
    -   **IN**: Restricted to the last column of the partition key to search multiple partitions.
    -   **Range (>=, <=, >, and <) on tokens**: Fully tokenized partition key (all partition key columns specified in order as arguments of the token function). Use token ranges to scan data stored on a particular node.

    **Note:** For secondary index queries, equals is the only operator supported for partition key logical statements.

    See Partition keys for examples and instructions.

clustering_conditions
    Use logic statements that identify the clustering segment. Clustering columns set the sort order of the stored data, which is nested when there are multiple clustering columns. After evaluating the partition key, the database evaluates the clustering statements in the nested order, the first (top level), second, third, and so on.

    All operators are supported in logical statements if the table has only one clustering column. To efficiently locate the data within the partition for tables with multiple clustering columns, the following restrictions apply:

    -   All clustering columns excluding the last clustering column:
        -   Equals (=)
        -   IN
    -   Last clustering column: All equality and inequality operators, and multi-column comparisons

    Clustering column logic statements also support returning slices across clustering segments:

    
    ( column1, column2, ... ) operator ( value1, value2, ... )
    [ AND ( column1, column2, ... ) operator ( value1, value2, ... ) ]
    

    The slice identifies the row that has the corresponding values and allows you to return all rows before, after, or between (when two slice statements are included).

    See Clustering columns for examples and instructions.

index_conditions

DSE supports these index types:

Secondary index
    Logical statements on secondary index columns support these operators:

    -   =
    -   CONTAINS on index collection types
    -   CONTAINS KEY on index map types

Solr query
    Filter the query using the `solr_query` option by creating a Solr expression. See Search index syntax.

SASI index
    To retrieve data using a SSTable Attached Secondary Index, see Using SASI.

Additional options

Change the scope and order of the data returned by the query.

GROUP BY column_name | function_name( argument_list )
    Condenses the selected rows that share the same values for a set of columns or values returned by a function into a group.

ORDER BY ( ASC | DESC )
    Sorts the result set in either ascending (ASC) or descending (DESC) order.

    **Note:** When no order is specified, the results are returned in the order that they are stored.

ALLOW FILTERING
    Enables filtering without applying logic statements that identify the primary key. Avoid `ALLOW FILTERING` in a production environment because a full scan of the cluster is performed.

    **Note:** See Allow Filtering explained.

LIMIT *N* | PER PARTITION LIMIT *N*
    Limits the number of records returned in the result set.


'''
