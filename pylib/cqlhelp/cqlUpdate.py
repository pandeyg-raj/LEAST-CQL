# coding: utf-8
'''
UPDATE

Modifies one or more column values to a row in a table.

Synopsis


UPDATE [keyspace_name.]table_name
  [ USING TTL time_value ]
  [ [ AND ] USING TIMESTAMP timestamp_value ]
  SET assignment [ , assignment ... ] 
  WHERE row_specification
  [ IF EXISTS | IF condition [ AND condition ] ] ;


**Note:** To modify a base table that has a materialized view (MV) using an `INSERT` or `UPDATE` command if access permissions are enabled, a user must be granted `MODIFY` or `ALL PERMISSIONS` on the base table.

keyspace_name
    The name of the keyspace containing the table to be updated. Not needed if the keyspace has been set for the session with the USE command.

table_name
    The name of the table to be updated.

time_value
    The value for TTL is a number of seconds. Column values in a command marked with TTL are automatically marked as deleted (with a tombstone) after the specified number of seconds. The TTL applies to the marked column values, not the column itself. Any subsequent update of the column resets the value to the TTL specified in the update. By default, values never expire. You cannot set a time_value for data in a counter column.

    **Warning:** The database storage engine can only encode TTL timestamps through `January 19 2038 03:14:07 UTC` due to the Year 2038 problem. The TTL date overflow policy determines whether requests with expiration timestamps later than the maximum date are rejected or inserted. See -Dcassandra.expiration_date_overflow_policy.

timestamp_value
    If TIMESTAMP is used, the inserted column is marked with its value – a timestamp in microseconds. If a TIMESTAMP value is not set, the database uses the time (in microseconds) that the update occurred to the column.

assignment
    Assigns a value to an existing element.

row_specification
    The `WHERE` clause must identify the row or rows to be updated by primary key.

IF EXISTS | IF condition
    Performs validation before updating records (lightweight transaction). Use as follows:

    -   `IF EXISTS` - One or more rows must match the query. If no rows match, the statement fails.

        
        UPDATE cycling.cyclist_name
        SET comment = 'Rides hard, gets along with others, a real winner'
        WHERE id = fb372533-eb95-4bb4-8685-6ef61e994caa;
        
        UPDATE cycling.cyclist_name
        SET comment = 'Rides fast, does not get along with others, a real dude'
        WHERE id = 5b6962dd-3f90-4c93-8f61-eabfa4a803e2;
        UPDATE cycling.cyclist_name
        SET comment = 'Rides hard, gets along with others, a real winner'
        WHERE id = fb372533-eb95-4bb4-8685-6ef61e994caa 
        IF EXISTS;
        UPDATE cycling.cyclist_name
        SET firstname = 'Roxane'
        WHERE id = 4647f6d3-7bd2-4085-8d6c-1229351b5498
        IF firstname = 'Roxxane';
        

        **Tip:** When no rows match an UPDATE statement that does not have `IF EXISTS`, a new record is created.

    -   `IF conditional_statement` - Test non-primary key columns on rows that match the query. Applies the update to rows that return true. If no rows match the query and the conditional statement tests for NULL, a new record is inserted.

        
        UPDATE cycling.cyclist_name
        SET comment = 'Rides hard, gets along with others, a real winner'
        WHERE id = fb372533-eb95-4bb4-8685-6ef61e994caa 
        IF comment = NULL;
        


    **Warning:** Using IF statements impact performance, see linearizable consistency.

    For examples, see Conditionally updating columns.


'''
