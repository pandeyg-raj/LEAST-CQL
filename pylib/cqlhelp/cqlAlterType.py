# coding: utf-8
'''
ALTER TYPE

Modifies an existing user-defined type (UDT).

**Restriction:** Modifying UDTs used in primary keys or index columns is not supported. Changing the field type is not supported.

Synopsis


ALTER TYPE field_name 
  ( ADD field_name cql_datatype
  | RENAME field_name TO new_field_name [ AND field_name TO new_field_name ...] ) ;


ADD (field_namecql_datatype[,...])
    Add fields by entering a field name followed by the data type in a comma-separated list; the values for existing rows is set to null.

RENAME field_name TO new_field_name
    Enter the old name and new name of the field.

AND
    Use between clauses to make multiple changes.


'''
