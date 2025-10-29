# coding: utf-8
'''
ALTER SEARCH INDEX CONFIG

Modify the search index *pending* configuration.

Use the CQL shell command DESCRIBE SEARCH INDEX to view the pending and active search index. Use the RELOAD SEARCH INDEX command to apply changes to the active configuration.

**Restriction:** Command available only on DSE Search nodes. Running search index management commands on large datasets can take longer than the CQLSH default timeout of 10 minutes. Increase the CQLSH client timeout as required.

Synopsis


ALTER SEARCH INDEX CONFIG ON [keyspace_name.]table_name
  ( ADD element_path [ attribute_list ] WITH $$ json_map $$
  | SET element_identifier = 'value'
  | SET shortcut = value
  | DROP element_identifier
  | DROP shortcut ) ;


keyspace_name.table_name
    Identifies the table of the search index; keyspace name is required when the table is not in the active keyspace.

element_path
    Identifies the XML path to the setting. Separate child elements using a period. For example:

    
    types.fieldTypes
    

attribute_list
    A comma-separated list of attributes value pairs enclosed in braces using the following syntax:

    
    [@attribute_name = 'value', 
    @attribute_name = 'value', ... ]
    

json_map
    Advanced. Use JSON format to define child elements, such as analyzer tokenizer and filter definitions of field type.

    
    { "element_name" : [ 
                      { "child_element_name" : { "child_attribute_name" : "value" } } ,
                      { "child_element_name" : { "child_attribute_name" : "value" } }, ... ],
    "element_name" : [ 
                      { "child_element_name" : { "child_attribute_name" : "value" } } ,
                      { "child_element_name" : { "child_attribute_name" : "value" } }, ... ], ... }
    

element_identifier
    Identifies the XML path to the setting. To locate an element with specific attribute, use the following syntax.

    
    element_name[@attribute_name='value']
    

shortcut
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


'''
