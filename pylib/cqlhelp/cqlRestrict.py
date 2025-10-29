# coding: utf-8
'''
RESTRICT

Use RESTRICT to deny access to a role on a data resource, that is a keyspace or table. Restrict denies access even if permission to access the resource has been granted.

**Note:**`RESTRICT` permission always take precedence over GRANT permissions.

Synopsis


RESTRICT permission
  ON [keyspace_name.]table_name 
  TO role_name ;


permission
    A comma separated list of permissions that the role is prevented from using on the resources even if the permissions is granted. Where the permission types are: `ALL PERMISSIONS` or `ALTER`, `AUTHORIZE [FOR permission_list]`, `CREATE`, `DESCRIBE`, `DROP`, `MODIFY`, and `SELECT`.

resource
    Database object to which the permission is denied. Restriction is applied using modeled hierarchy as follows:

    -   `ALL KEYSPACES` - restricts access to every keyspace and table.
    -   `KEYSPACE keyspace_name` - restricts access on the keyspace and any table it contains
    -   `TABLE table_name` - restricts access on the table and all the data it contains


'''
