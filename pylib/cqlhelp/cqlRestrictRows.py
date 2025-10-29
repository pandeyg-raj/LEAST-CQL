# coding: utf-8
'''
RESTRICT ROWS

Configures the column used for row-based access control; you can only define one Primary Key column. If the column is already configured, running the RESTRICT ROWS command replaces the definition.

**Tip:** Use DESCRIBE TABLE to view the existing restrictions on the table.

Synopsis


RESTRICT ROWS 
  ON [keyspace_name.]table_name 
  USING pk_column_name ;



'''
