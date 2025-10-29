# coding: utf-8
'''
ALTER KEYSPACE

Modifies the keyspace replication strategy, which is the number of copies of the data in each datacenter, cqlCreateKeyspace.py#CQLreplicationMap, and/or disable the commit log for writes, Durable Writes.

**Note:** Datacenter names are case-sensitive. Verify the case of the using utility, such as `dsetool status`.

**Restriction:** Changing the keyspace name is not supported.

Synopsis


ALTER KEYSPACE keyspace_name 
  WITH REPLICATION = { replication_map }
  [ AND DURABLE_WRITES = ( true | false ) ]
  [ AND graph_engine =  'Core' ];


replication_map
    'class' : 'SimpleStrategy', 'replication_factor' : N

    Assigns the same replication factor to the entire cluster. Use for evaluation and single datacenter test and development environments only.

    'class' : 'NetworkTopologyStrategy', 'datacenter_name' : N, ...

    After the class declaration, assign replication factors to each datacenter by name in a comma-separated list. Use in production environments and multi-DC test and development environments. Datacenter names must match the snitch DC name; see Snitches.

    **Important:** Use only replication strategy implementations bundled with DSE.

DURABLE_WRITES = true | false
    Optional. Although not recommended, can be changed to false, to bypass the commit log when writing to the keyspace. Default value is `true`.

graph_engine = 'Core'
    Optional. Use to treat a Cassandra keyspace as a graph. Only the 'Core' engine can be specified; the 'Classic' engine cannot.


'''
