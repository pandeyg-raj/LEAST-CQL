# coding: utf-8
'''
LIST PERMISSIONS

List of permissions. Filter list by resource and/or role.

**Restriction:**

-   Only superusers can list all permissions.
-   Requires `DESCRIBE` permission on the target resources and roles.

Synopsis


LIST ( ALL PERMISSIONS | permission_list )
  [ ON resource_name ]
  [ OF role_name ] 
  [ NORECURSIVE ] ;


**Tip:** Omit `ON resource_name to display all related resources` or omit `OF role_name` to display all role permissions.

List options

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

role_name
    Selects a role. If the role name has capital letters or special characters enclose it in single quotes.

NORECURSIVE
    Only display permissions granted to the role. By default permissions checks are recursive; it shows direct and inherited permissions.

List output

The list command shows the following information:


list all permissions of role1;

 role  | username | resource           | permission | granted | restricted | grantable
-------+----------+--------------------+------------+---------+------------+-----------
 role1 |    role1 | <keyspace cycling> |       DROP |   False |       True |      True
 role1 |    role1 | <keyspace cycling> |  AUTHORIZE |    True |       True |     False
 role2 |    role2 | <keyspace cycling> |     CREATE |    True |      False |     False
 role3 |    role3 | <keyspace cycling> |       DROP |   False |      False |      True
 role3 |    role3 | <keyspace cycling> |     MODIFY |    True |      False |     False

(5 rows)


**Output columns**
role
    The name of the role that the permission was granted or authorized on.

username
    If the role is associated with a legacy user account the user name displays, else the role name displays.

resource
    The resource name in angle brackets.

permission
    The name of the permission.

    **Tip:** When `ALL PERMISSIONS` is used, each type of permission associated with the resource is granted.

granted
    -   `True` - Execute commands granted by the permission on the resource. When AUTHORIZE is granted equals true, the users with the role can grant other permissions that have granted to them on the resource to other roles.
    -   `False` - Users cannot execute the permission commands.

restricted
    -   `True` - Denies execution of the commands associated with the permission on the resource even if granted is true. If grantable is true, users with the role can still AUTHORIZE roles other than their own.
    -   `False` - Users can execute commands that have granted equal to true.

grantable
    -   `True` - Allows grant or revoke of the permission on the resource to another role, other than any of their own roles.
    -   `False` - AUTHORIZE FOR permission has not been granted.


'''
