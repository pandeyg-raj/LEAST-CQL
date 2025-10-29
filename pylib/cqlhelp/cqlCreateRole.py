# coding: utf-8
'''
CREATE ROLE

Creates a cluster wide database object used for access control to database resources, such as keyspaces, tables, functions. Use roles to:

-   Define a set of permissions that can be assigned to other roles and mapped to external users.
-   Create login accounts for internal authentication. (Not recommended for production environments.)

**Warning:** A full access login account *cassandra* (password *cassandra*) is enabled by default; create your own full access role and drop the *cassandra* account.

Synopsis


CREATE ROLE [ IF NOT EXISTS ] role_name
  [ WITH [ SUPERUSER = ( true | false ) ] 
  [ [ AND ] LOGIN = ( true | false ) ] 
  ( WITH PASSWORD 'role_password' |
  WITH HASHED PASSWORD 'hashed_role_password' )
  [ [ AND ] OPTIONS = { option_map } ] ] ;


role_name
    Use a unique name for the role. DataStax Enterprise forces all names to lowercase; enclose in quotes to preserve case or use special characters in the name.

    **Note:** To automatically map external users to roles with DSE Unified Authenticator, the role name must exactly match the LDAP group name, including case.

SUPERUSER
    True automatically grants AUTHORIZE, CREATE and DROP permission on ALL ROLES.

    Superusers can only manage roles by default. To manage other resources, you must grant the permission set to that resource. For example, to allow access management for all keyspaces: `GRANT ALL PERMISSIONS ON ALL KEYSPACES TO role_name`.

    Default: false.

LOGIN
    True allows the role to log in. Use true to create login accounts for internal authentication, PasswordAuthenticator, or DSE Unified Authenticator.

    Default: false.

WITH PASSWORD | WITH HASHED PASSWORD
    Enclose the password or hashed password in single quotes. Internal authentication requires a password or hashed password.

    **Note:** Roles for users authenticated by an external directory, such as DSE Unified Authenticator, must have login enabled with no password or hashed password.

OPTIONS = { option_map }
    Reserved for use with authentication plug-ins. Refer to the authenticator documentation for details.


'''
