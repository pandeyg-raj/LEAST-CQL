# coding: utf-8
'''
REBUILD SEARCH INDEX

Rebuilds the search index. Re-constructs the index after changes to the index schema, such as adding or removing fields, adding a copy field or changing field settings. Queries using the solr_query option may return no results, partial, or old data while the index is rebuilding.

**Note:** Use the RELOAD command to replace the active search index with the pending version.

**Restriction:** Command available only on DSE Search nodes. Running search index management commands on large datasets can take longer than the CQLSH default timeout of 10 minutes. Increase the CQLSH client timeout as required.

Synopsis


REBUILD SEARCH INDEX ON [keyspace_name.]table_name
  [ WITH OPTIONS { deleteAll : ( true | false ) } ] ;


OPTIONS

The request option configures the entire request to specify whether to delete the existing index:

deleteAll
    -   `true` Completely replaces the existing index. Use when changes to the schema affect the way that data is physically stored, such as changes to the field type analyzer, a column data type, etc.
    -   `false` (Default.) Keeps existing search index data. Reindexing happens in-place; search results will return partially incorrect results while the index is updating. Keep the current index (accepting reads) while you build the new one, then swap over to the new index after it's ready. Use when table columns are removed or added to the index.


'''
