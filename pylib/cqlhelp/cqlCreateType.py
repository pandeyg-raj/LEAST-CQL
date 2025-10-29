# coding: utf-8
'''
CREATE TYPE

Creates a custom data type in the keyspace that contains one or more fields of related information, such as address (street, city, state, and postal code).

**Restriction:** UDTs cannot contain counter fields.

Synopsis


CREATE TYPE [ IF NOT EXISTS ] [keyspace_name].type_name
  (field_name cql_datatype [ , field_name cql_datatype ... ]) ;


IF NOT EXISTS
    Suppresses the error if the type already exists in the keyspace. UDT scope is keyspace-wide.

type_name
    Unique name for the type. CQL types are reserved for a list. See type names.

field_namecql_datatype
    Define fields that are in the UDT in a comma-separated list: `field_namecql_datatype, field_name, cql_datatype`.


'''
