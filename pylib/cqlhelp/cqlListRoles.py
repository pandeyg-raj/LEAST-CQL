# coding: utf-8
'''
LIST ROLES

Lists roles and shows superuser and login status. This command runs with a consistency level of ``QUOROM``.

**Restriction:** Roles have describe permission on their own and any inherited roles. Only roles that the current user has permission to see is listed.

Synopsis


LIST ROLES 
  [ OF role_name ] 
  [ NORECURSIVE ] ;



'''
