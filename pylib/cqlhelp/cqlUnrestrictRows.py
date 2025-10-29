# coding: utf-8
'''
UNRESTRICT ROWS

Removes the column definition for row-level access to roles.

**Note:** When no column is selected, roles that have been granted access on rows (but not the table or keyspace) no longer have access. To restore or change the selected column for RLAC, use the RESTRICT ROWS command.

Synopsis


UNRESTRICT ROWS ON [keyspace_name.]table_name ; 



'''
