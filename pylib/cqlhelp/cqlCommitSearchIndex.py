# coding: utf-8
'''
COMMIT SEARCH INDEX

Forces an update of the search index with the most recent data after executing an INSERT, UPDATE, or DELETE statement.

**Note:** By default, changes are automatically committed every 10000 milliseconds. To change the default setting see Changing the autocommit time.

**Restriction:** Command available only on DSE Search nodes. Running search index management commands on large datasets can take longer than the CQLSH default timeout of 10 minutes. Increase the CQLSH client timeout as required.

Synopsis


COMMIT SEARCH INDEX ON [keyspace_name.]table_name ;



'''
