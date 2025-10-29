# coding: utf-8
'''
ALTER USER (Deprecated)

Alter existing user options.

**Note:** Deprecated. `ALTER USER` is supported for backwards compatibility only. Use ROLE for authentication and authorization.

Synopsis


ALTER USER user_name 
  ( WITH PASSWORD 'user_password' |
  WITH HASHED PASSWORD 'hashed_user_password' )
  [ ( SUPERUSER | NOSUPERUSER ) ] ;



'''
