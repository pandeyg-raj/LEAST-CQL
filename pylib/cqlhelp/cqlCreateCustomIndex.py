# coding: utf-8
'''
CREATE CUSTOM INDEX (SASI)

Generates SSTable Attached Secondary Index (SASI) on a table column.

SASI uses significantly using fewer memory, disk, and CPU resources. It enables querying with PREFIX and CONTAINS on strings, similar to the SQL implementation of `LIKE = "foo*"` or `LIKE = "*foo*"`.

**Attention:** SASI indexes in DSE are experimental. DataStax does not support SASI indexes for production.

For more information about SASI, see Using SASI.

Synopsis


CREATE CUSTOM INDEX [ IF NOT EXISTS ] [ index_name ]
  ON [keyspace_name.]table_name (column_name)
  USING 'org.apache.cassandra.index.sasi.SASIIndex' 
  [ WITH OPTIONS = { option_map } ] ;


index_name
    Optional identifier for index. If no name is specified, the default is used, `table_name_column_name_idx`. Enclose in quotes to use special characters or preserve capitalization.

OPTIONS
    Define options in JSON simple format.


'''
