# coding: utf-8
'''
CREATE KEYSPACE

Creates a top-level keyspace. Configure the replica placement strategy, replication factor, and durable writes setting.

**Important:** Use only replication strategy implementations bundled with DSE.


CREATE KEYSPACE [ IF NOT EXISTS ] keyspace_name 
  WITH REPLICATION = { replication_map }
  [ AND DURABLE_WRITES = ( true | false ) ]
  [ AND graph_engine = 'Core' ] ;


keyspace_name
    Maximum of 222 characters. Can contain alpha-numeric characters and underscores; only letters and numbers are supported as the first character. Unquoted names are forced to lowercase.

replication_map
    The replication map determines how many copies of the data are kept in a given datacenter. This setting impacts consistency, availability and request speed, for more details see replica placement strategy.

DURABLE_WRITES = true | false
    Optional. Although not recommended, can be changed to false, to bypass the commit log when writing to the keyspace. Default value is `true`.

graph_engine = 'Core'
    Optional. Use to treat a Cassandra keyspace as a graph. Only the 'Core' engine can be specified; the 'Classic' engine cannot.


'''
