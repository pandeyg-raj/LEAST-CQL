# coding: utf-8
'''
DROP TABLE

Immediate, irreversible removal of a table, including all data contained in the table.

**Restriction:**Drop all materialized views associated with the table before dropping the table. An error message lists any materialized views that are based on the table: `InvalidRequest: Error from server: code=2200 [Invalid query] message="Cannot drop table when materialized views still depend on it (cycling.{cyclist_by_age})"`

Synopsis


DROP TABLE [ IF EXISTS ] [keyspace_name.]table_name ;



'''
