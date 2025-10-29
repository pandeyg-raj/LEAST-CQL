# coding: utf-8
'''
BATCH

Combines multiple data modification language (DML) statements (such as INSERT, UPDATE, and DELETE) to achieve atomicity and isolation when targeting a single partition, or only atomicity when targeting multiple partitions.

**Tip:** See Batching inserts, updates, and deletes.

A batch applies all DML statements within a single partition before the data is available, ensuring atomicity and isolation. A well-constructed batch targeting a single partition can reduce client-server traffic and more efficiently update a table with a single row mutation.

For multiple partition batches, logging ensures that all DML statements are applied. Either all or none of the batch operations will succeed, ensuring atomicity. Batch isolation occurs only if the batch operation is writing to a single partition.

**Important:** Only use a multiple partition batch when there is no other viable option, such as asynchronous statements. Multiple partition batches may decrease throughput and increase latency.

Optionally, a batch can apply a client-supplied timestamp. Before implementing or executing a batch see Batching inserts and updates.

Batches are not isolated among client programs. Other client programs can read the first modified rows from the batch while the other remaining statements in the batch are in progress. There is no batch rollback functionality, which means that a batch cannot be undone.

Synopsis


BEGIN [ ( UNLOGGED | LOGGED ) ] BATCH 
  [ USING TIMESTAMP [ epoch_microseconds ] ]
  dml_statement [ USING TIMESTAMP [ epoch_microseconds ] ] ;
  [ dml_statement [ USING TIMESTAMP [ epoch_microseconds ] ] [ ; ... ] ] ;
  APPLY BATCH ;


A batch can contain these dml_statements:

-   **`INSERT`**
-   **`UPDATE`**
-   **`DELETE`**

UNLOGGED | COUNTER
    If `UNLOGGED` is not specified, the batch is logged. If multiple partitions are involved, batches are logged by default. A logged batch ensures that all or none of the batch operations succeed (atomicity). First the serialized batch is written to the batchlog system table which consumes the serialized batch as blob data. After a successful write, the rows are persisted (or hinted) and the batchlog data is removed. Logging incurs a performance penalty, the batchlog is written to two other nodes. Options for thresholds, warning about or failure due to batch size, are available.

    `UNLOGGED` runs the batch without logging penalties. Unlogged batching issues a warning when too many operations or too many partitions are involved. Single partition batch operations are unlogged by default, and are the only unlogged batch operations recommended.

    Use the `COUNTER` option for batched counter updates. Unlike other updates, counter updates are not idempotent.

USING TIMESTAMPS
    Sets the write time for transactions executed in a BATCH.

    **Restriction:**`USING TIMESTAMP` does not support LWT (lightweight transactions), such as DML statements that have an `IF NOT EXISTS` clause.


'''
