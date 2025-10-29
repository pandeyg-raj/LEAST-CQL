# coding: utf-8
'''
REVOKE

Removes privileges on database objects from a role.

CAUTION:

`REVOKE` does not automatically invalidate cached permissions. Permissions are invalidated the next time they are refreshed.

Synopsis


REVOKE permission 
  ON resource_name
  FROM role_name ;


permission
    Type of access a role has on a database resource. Use `ALL PERMISSIONS` or a comma separated list of permissions.

    Permissions are resource specific as follows:

    -   **Data** - `ALL PERMISSIONS` or `ALTER`, `AUTHORIZE [FOR permission_list]`, `CREATE`, `DESCRIBE`, `DROP`, `MODIFY`, and `SELECT`
    -   **Functions (and aggregates)** - `ALL PERMISSIONS` or `ALTER`, `AUTHORIZE [FOR permission_list]`, `CREATE`, and `DROP`
    -   **Search indexes** - `AUTHORIZE [FOR permission_list]`, `SEARCH.ALTER`, `SEARCH.COMMIT`, `SEARCH.CREATE`, `SEARCH.DROP`, `SEARCH.REBUILD`, and `SEARCH.RELOAD`
    -   **Roles** - `ALL PERMISSIONS` or `ALTER`, `AUTHORIZE [FOR permission_list]`, `CREATE`, `DESCRIBE`, `DROP`, `PROXY.EXECUTE`, and `PROXY.LOGIN`
    -   **JMX (MBeans)** - `ALL PERMISSIONS` or `AUTHORIZE [FOR permission_list]`, `DESCRIBE`, `EXECUTE`, `MODIFY`, and `SELECT`
    -   **Remote procedure calls (RPC)** - `ALL PERMISSIONS` or `AUTHORIZE [FOR permission_list]`, `EXECUTE`, `MODIFY`, and `SELECT`
    -   **Authentication schemes** - `ALL PERMISSIONS` or `AUTHORIZE [FOR permission_list]` and `EXECUTE`
    -   **Spark workpools** - `ALL PERMISSIONS` or `AUTHORIZE [FOR permission_list]`, `CREATE`, and `DESCRIBE`
    -   **Spark submissions** - `ALL PERMISSIONS` or `AUTHORIZE [FOR permission_list]`, `DESCRIBE`, and `MODIFY`

    **Note:** To manage access control the role must have authorize permission on the resource for the type of permission. When AUTHORIZE is granted without specifying `FOR permission`, the role can manage all permissions on the object.

resource_name
    DataStax Enterprise database objects on which permissions are applied. Database resources have modelled hierarchy, the permission on a top level object gives the role the same permission on the objects ancestors. Identify the resource using the following keywords:

    -   Data - `ALL KEYSPACES` > `KEYSPACE`keyspace_name > `TABLE table_name` > `'filtering_data' ROWS IN table_name`
    -   Function (including aggegrates) - `ALL FUNCTIONS`, `ALL FUNCTIONS IN KEYSPACE keyspace_name`, and `FUNCTION keyspace_name.function_name( argument_types)`
    -   Search indexes - `ALL SEARCH INDICES` > SEARCH KEYSPACE keyspace_name > `SEARCH INDICES [keyspace_name.]table_name`
    -   JMX MBeans - `ALL MBEANS > MBEAN mbean_name` and `MBEANS pattern`
    -   Remote procedure calls (RPC) - `ALL REMOTE CALLS` > `REMOTE METHOD name` | `REMOTE OBJECT name`
    -   Roles - `ALL ROLES` > `ROLE role_name`
    -   Authentication schemes - `ALL SCHEMES` > `LDAP` | `KERBEROS` | `INTERNAL`
    -   Analytic applications
        -   Workpools - `ANY WORKPOOL` > `WORKPOOL 'dc_name.*'` > `WORKPOOL 'dc_name.workpool_name'`
        -   Submissions - `ANY SUBMISSION` > `ANY SUBMISSION IN WORKPOOL 'datacenter_name.*' > 'datacenter_name.workpool_name' > SUBMISSION ID`


'''
