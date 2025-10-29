# coding: utf-8
'''
CREATE USER (Deprecated)

`CREATE USER` is supported for backwards compatibility only. Authentication and authorization for DataStax Enterprise 5.0 and later are based on `ROLES`, and use `CREATE ROLE` instead.

`CREATE USER` defines a new database user account. By default users accounts do not have superusersuperuser status. Only a superuser can issue `CREATE USER` requests. See CREATE ROLE for more information about `SUPERUSER` and `NOSUPERUSER`.

User accounts are required for logging in under internal authentication and authorization.

Enclose the user name in single quotation marks if it contains non-alphanumeric characters. You cannot recreate an existing user. To change the superuser status, password or hashed password, use ALTER USER.

Synopsis


CREATE USER [ IF NOT EXISTS ] user_name 
  ( WITH PASSWORD 'user_password' |
  WITH HASHED PASSWORD 'hashed_user_password' )
  [ ( SUPERUSER | NOSUPERUSER ) ] ;



'''
