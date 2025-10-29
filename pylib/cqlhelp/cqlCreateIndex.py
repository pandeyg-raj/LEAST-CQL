# coding: utf-8
'''
CREATE INDEX

Define a new index on a single column of a table. If the column already contains data, it is indexed during the execution of this statement. After an index has been created, it is automatically updated when data in the column changes. DataStax Enterprise supports creating an index on most columns, including the partition and cluster columns of a PRIMARY KEY, collections, and static columns. Indexing can impact performance. Before creating an index, be aware of when and when not to create an index.

**Restriction:** Indexing counter columns is not supported. For maps, index the key, value, or entries.

Synopsis


CREATE INDEX [ IF NOT EXISTS ] index_name
  ON [keyspace_name.]table_name 
  ([ ( KEYS | FULL ) ] column_name) 
  (ENTRIES column_name) ;


index_name
    Optional identifier for index. If no name is specified, DataStax Enterprise names the index: `table_name_column_name_idx`. Enclose in quotes to use special characters or preserve capitalization.


'''
