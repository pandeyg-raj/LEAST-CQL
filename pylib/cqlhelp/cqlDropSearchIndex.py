# coding: utf-8
'''
DROP SEARCH INDEX

Drops a search index from a table and optionally deleted the resources associated with the search index.

**Restriction:** Command available only on DSE Search nodes. Running search index management commands on large datasets can take longer than the CQLSH default timeout of 10 minutes. Increase the CQLSH client timeout as required.

The request options are boolean values:

deleteResources
    -   true - deletes the resources associated with the search index.
    -   false - does not delete the resources.

    Default: true

deleteDataDir
    -   true - deletes index data and any other artifacts in the solr.data directory. It does **not** delete data from the database.
    -   false - does not delete index data.

    Default: false


'''
