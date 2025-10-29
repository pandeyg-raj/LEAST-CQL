# coding: utf-8
'''
RELOAD SEARCH INDEX

Changes made using ALTER SEARCH INDEX CONFIG or ALTER SEARCH INDEX SCHEMA are marked PENDING. Use the RELOAD command to replace the active search index with the pending version. Use the CQL shell command DESCRIBE SEARCH INDEX to view pending and active search index schema and config.

**Note:** Run REBUILD SEARCH INDEX after changing the schema to reindex existing data.

**Restriction:** Command available only on DSE Search nodes. Running search index management commands on large datasets can take longer than the CQLSH default timeout of 10 minutes. Increase the CQLSH client timeout as required.

Synopsis


RELOAD SEARCH INDEX ON [keyspace_name.]table_name ;



'''
