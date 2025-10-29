# coding: utf-8
'''
ALTER SEARCH INDEX SCHEMA

Modify the search index *pending* schema.

Use the RELOAD SEARCH INDEX command to apply changes to the active schema.

**Note:** Space saving profiles apply only to the initial creation of the search index. For example, if the index was created using a resource_generation_profiles, like `spaceSavingSlowTriePrecision`, and later a numeric column is added to the index using the ALTER command, the trie fields precisionStep of the new column is not set to '0'.

**Restriction:** Command available only on DSE Search nodes. Running search index management commands on large datasets can take longer than the CQLSH default timeout of 10 minutes. Increase the CQLSH client timeout as required.

Synopsis


ALTER SEARCH INDEX SCHEMA ON [keyspace_name.]table_name
  ( ADD field column_name
  | ADD element_path [ attribute_list ] WITH $$ json_map $$
  | SET element_identifier = 'value'
  | DROP field field_name
  | DROP element_identifier ) ;


    **Variables**

keyspace_name.table_name
    Identifies the table of the search index; keyspace name is required when the table is not in the active keyspace.

column_name
    Identifies a table column. The search index field and associated type are automatically defined.

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
    

ADD
    Insert a new type, field, or other settings in the pending schema.

DROP
    Remove a table column that corresponds directly to a field or one of the following configurations from the pending schema. The required attributes by element are:

    -   `field` - `name` attribute
    -   `fieldType` - `name` attribute
    -   `dynamicField` - `name` attribute
    -   `copyField` - `source` and `dest`

    See Managing search index fields and Dropping columns from the index in the documentation.

SET
    Change the configuration of a setting in the pending schema.


'''
