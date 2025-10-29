# coding: utf-8
'''
ALTER ROLE

Changes password or hashed password and sets superuser or login options.

Synopsis


ALTER ROLE role_name 
  [ ( WITH PASSWORD 'role_password' |
  WITH HASHED PASSWORD 'hashed_role_password' ) ]
  [ [ AND ] LOGIN = ( true | false ) ] 
  [ [ AND ] SUPERUSER = ( true | false ) ] 
  [ [ AND ] OPTIONS = { option_map } ] ] ;


WITH PASSWORD | WITH HASHED PASSWORD
    Change the password or hashed password of the logged in role. Superusers (and roles with ALTER PERMISSION to a role) can also change the password or hashed password of other roles.

SUPERUSER
    Enable or disable superuser status for another role, that is any role other than the one that is currently logged in. Setting superuser to false, revokes permission to create new roles; disabling does not automatically revoke the AUTHORIZE, ALTER, and DROP permissions that may already exist.

LOGIN
    Enable or disable log in for roles other than currently logged in role.

OPTIONS
    Reserved for external authenticator plug-ins.


'''
