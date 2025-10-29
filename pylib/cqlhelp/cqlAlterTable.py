# coding: utf-8
'''
ALTER TABLE

Add new columns, drop existing columns, renames columns, and modify table or graph properties. The command returns no results.

**Restriction:**

-   Can only rename clustering columns in the primary key.
-   Cannot change the data type of a column.
-   For a table that has a materialized view, cannot drop a column from the table even if the column is not used in the materialized view.
-   Cannot rename or drop columns that have dependent secondary indexes or Datastax Enterprise Search indexes.
-   Do not add a column with the same name as an existing column but with a different data type. It will prevent commit log replays and corrupt existing SSTables with old data.

Synopsis


ALTER TABLE [keyspace_name.]table_name 
  [ ADD ( column_definition | column_definition_list ) [ , ... ] ]
  [ DROP column_name [ , ... ] ]
  [ [ RENAME column_name TO column_name ] |
    [ RENAME ( VERTEX LABEL | EDGE LABEL ) TO new_name ] ]
  [ WITH table_properties [ , ... ] ] 
  [ WITH ( VERTEX LABEL | EDGE LABEL ) current_name ]
  [ WITHOUT ( VERTEX LABEL | EDGE LABEL ) current_name ];


ADD column_definition | ( column_definition_list )
    Add one or more columns and set the column data types. Specify the column names followed by the data types. The column value is automatically set to null. To add multiple columns, use a comma separated list of columns placed inside parentheses.

    **Restriction:** Adding columns to a primary key is not supported after a table has been created.

DROP column | ( column_list )
    Drop one or more columns. The values contained in the row are also dropped and not recoverable. To drop multiple columns, use a comma separated list of columns placed inside parentheses.

RENAME column_name TO column_name
    Changes the name of a primary key column and preserves the existing values.

    **Restriction:** Not supported on materialized view base-tables, or tables with secondary indexes or Datastax Enterprise Search indexes.

RENAME ( VERTEX LABEL | EDGE LABEL ) TO new_name
    Changes the name of a vertex label or edge label associated with the table.

    **Restriction:** Not supported on materialized view base-tables, or tables with secondary indexes or Datastax Enterprise Search indexes.

WITH ( VERTEX LABEL | EDGE LABEL ) current_name
    Alter a table and associate a vertex label or edge label it.

    **Restriction:** Not supported on materialized view base-tables, or tables with secondary indexes or Datastax Enterprise Search indexes.

WITHOUT ( VERTEX LABEL | EDGE LABEL ) current_name
    Removes a vertex label or edge label associated with the table.

    **Restriction:** Not supported on materialized view base-tables, or tables with secondary indexes or Datastax Enterprise Search indexes.

table_properties
    You can modify an existing table's properties. Some properties are single options that are set to a value:

    
    option_name = value [ AND ... ]
    

    Other table properties are set using a JSON map: `option_name = { subproperty_name : value [ , ... ] }`


'''
