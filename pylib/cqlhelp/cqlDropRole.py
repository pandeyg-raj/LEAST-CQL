# coding: utf-8
'''
DROP ROLE

Removes an existing role. Enclose role names with special characters and capitalization in single quotation marks.

**Restriction:** The role used to drop roles must have `DROP` permission, directly or on `ALL ROLES` or the selected role. Only superuser roles can drop another superuser role. A role can never drop their own role.

Synopsis


DROP ROLE [ IF EXISTS ] role_name ;



'''
