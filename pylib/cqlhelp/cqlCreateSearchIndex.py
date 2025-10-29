# coding: utf-8
'''
CREATE SEARCH INDEX

Defines a new search index for an existing table. Automatically creates the search index schema and configuration, then generates an index.

**Restriction:** Command available only on DSE Search nodes. Running search index management commands on large datasets can take longer than the CQLSH default timeout of 10 minutes. Increase the CQLSH client timeout as required.

**Important:** This command runs with a consistency level of LOCAL_QUORUM because this command is only executed in the current datacenter.

Synopsis


CREATE SEARCH INDEX [ IF NOT EXISTS ] ON [keyspace_name.]table_name
  [ WITH [ COLUMNS column_list { option : value } [ , ... ] ]
  [ [ AND ] PROFILES profile_name [ , ... ] ]
  [ [ AND ] CONFIG { option:value } [ , ... ] ]
  [ [ AND ] OPTIONS { option:value } [ , ... ] ] ] ;


If the CREATE SEARCH INDEX statement specifies no options, all columns are indexed using the default values.

COLUMNS

Defines which fields to include in index, sets index type, and creates non-tokenized fields for faceted search.


COLUMNS column_list { copyField : true | false }, 
column_list { docValues : true | false }, 
column_list { excluded : true | false }, 
column_list { indexed : true | false }


**Note:** When the COLUMNS option is used, any column not listed is excluded from the index by default, except PRIMARY KEY columns which must be indexed.

column_list
    A comma-separated list or * (for all columns). You can include tuple fields and subfields. Any column not listed is excluded from the index by default, except PRIMARY KEY columns, which must be indexed.

    -   A comma-separated list of all of the column_names, tuplefield, or tuplefield.subfield to include in the search index. When a subfield is selected for inclusion, parent fields are always included.
    -   For each column in the column_list, optionally specify true or false for copyField, docValues, excluded, or indexed.
    -   Asterisk (*) to select all columns.

    For example:

    
    COLUMNS column_name1, column_name2
    

    
    COLUMNS column_name1, column_name2 {copyField:true}
    

copyField: (true | false)
    Set to true to create a new field copied from the specified columns with type `StrField`. Duplicates the data from the original field into the new field. Use for columns that require both search and faceting.

    Default value is false.

docValues: ( true | false)
    Creates a forward index on each specified column. Setting is only valid on Solr types that extend TrieField, UUIDField, and StrField. Use on columns that are sorted or grouped (faceted). Default is true for TrieField and UUIDField types and false StrField types.

    Due to SOLR-7264, setting docValues to true on a boolean field in the Solr schema does not work. A workaround for boolean docValues is to use 0 and 1 with a TrieIntField.

    **Note:**Using spaceSavings profiles disables auto generation of DocValues.

excluded: (true | false)
    When using the COLUMNS option, exclude column from index:

    -   true - exclude the listed columns and all fields in the columns from the index.
    -   false - do not exclude the listed columns from the index. You must specify columns to include to include the columns in the index. Default when not specified.

    Excluded columns are not present in HTTP query results and singlePass queries.

indexed: (true | false)
    When using the COLUMNS option:

    -   true - include the specified fields in the index. Default when not specified.
    -   false - exclude the specified fields from the index.

    **Important:** Non-indexed columns are present in HTTP query results and `singlePass` queries only if they are included in the Solr schema.xml file. For more information, see Solr single-pass CQL queries.

PROFILES

Apply space saving options to minimize index size on initial creation. Specify spaceSavingAll or a comma separated list of profiles to apply.


PROFILES profile_name [, profile_name, ...]


**Note:** Profiles only apply to the initial index generation, and do not apply to the ALTER SEARCH INDEX SCHEMA command.

spaceSavingAll
    Applies all profiles.

spaceSavingNoJoin
    Excludes the hidden partition key required for joins across tables on search queries from the index. When used table joins on search index queries are not allowed.

spaceSavingSlowTriePrecision
    Sets trie fields precisionStep to '0', allowing for greater space saving but slower querying.

CONFIG

Configuration options override values in the Search index config file. The CONFIG option map can pass options with this syntax:


CONFIG { shortcut_name:value [, shortcut_name:value, ...] }


shortcuts
    Shortcuts to configuration element values using SET:

    -   `autoCommitTime` Default value is 10000.
    -   `defaultQueryField` Name of the field. Default not set.

        **Note:** Use SET to add. Use DROP to remove.

    -   `directoryFactory` Can be used as an alternative to the directoryFactoryClass option. The options are:
        -   'standard'
        -   'encrypted'
    -   `filterCacheLowWaterMark` Default is 1024.
    -   `filterCacheHighWaterMark` Default is 2048.
    -   `directoryFactoryClass` Specifies the fully-qualified name of the directory factory. Use in place of the directoryFactory option for directory factories other than the standard or encrypted directory factory.
    -   `mergeMaxThreadCount` Must configure with mergeMaxMergeCount. The default is the number of tpc_cores as configured in cassandra.yaml.
    -   `mergeMaxMergeCount` Must configure with mergeMaxThreadCount. The default calculated value is:

        
        max(max(<maxThreadCount * 2>, <num_tokens * 8>), <maxThreadCount + 5>)
        

        where num_tokens is the number of token ranges to assign to the virtual node (vnode) as configured in cassandra.yaml.

    -   `ramBufferSize` Default is 512.
    -   `realtime` Default is false.

OPTIONS

Request options configure the entire request. The OPTIONS map can pass options with this syntax:


OPTIONS { option:value [, option:value, ...] }


The request options are boolean values:

recovery
    -   true - if the search core is unable to load due to corrupted index, recovers it by deleting and recreating the index. The deleteAll flag is set based on the recovery flag unless deleteAll is specifically set.
    -   false - no recovery. Default.

reindex
    -   true - reindexes the data. Keeps the current index (accepting reads) while the new index is building. Default.
    -   false - does not reindex the data.

lenient
    -   true - Silently ignores fields if you encounter an unsupported column type during schema autogeneration.
    -   false - Raise error if you encounter an unsupported column type during schema autogeneration.

    **Note:** This option is no longer needed for SpatialRecursivePrefixTreeFieldType fields, which are now automatically indexed.


'''
