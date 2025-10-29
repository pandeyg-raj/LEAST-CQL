# coding: utf-8
'''
CREATE TABLE

Creates a new table in the selected keyspace. Use `IF NOT EXISTS` to suppress the error message if the table already exists; no table is created. A static column can store the same data in multiple clustered rows of a partition, and then retrieve that data with a single `SELECT` statement.

Tables support a single counter column.

Synopsis


CREATE TABLE [ IF NOT EXISTS ] [keyspace_name.]table_name
  ( column_definition [ , ... ] | PRIMARY KEY (column_list) )
  [ WITH [ table_options ]
  [ [ AND ] CLUSTERING ORDER BY [ clustering_column_name order ] ] 
  [ AND ( VERTEX LABEL vl_name | EDGE LABEL ) el_name FROM vl_name TO vl_name]
  [ [ AND ] ID = 'table_hash_tag' ] ] ;


column_definition

Enclosed in parentheses after the table name, use a comma-separated list to define multiple columns. All tables must have at least one primary key column. Each column is defined using the following syntax: `column_namecql_type_definition [STATIC | PRIMARY KEY] [, ...]`

**Restriction:**

-   When primary key is at the end of a column definition, that column is the only primary key for the table.
-   A table must have at least one `PRIMARY KEY`.
-   A static column cannot be a primary key.
-   Primary keys can include frozen collections.

column_name
    Use a unique name for each column in a table. To preserve case or use special characters, enclose the name in double-quotes.

cql_type_definition
    Defines the type of data allowed in the column. See CQL data type or a user-defined type.

STATIC
    Optional, the column has a single value.

PRIMARY KEY
    When the `PRIMARY KEY` is one column, append PRIMARY KEY to the end of the column definition. This is only schema information required to create a table. When there is one primary key, it is the partition key; the data is divided and stored by the unique values in this column:`column_namecql_type_definition PRIMARY KEY`.

    Alternatively, you can declare the primary key consisting of only one column in the same way as you declare a compound primary key.

PRIMARY KEY (column_list)

Uniquely identifies rows, determines storage partitions, and orders data (clustering columns) within a partition.

**Restriction:** Primary keys cannot have the following data types: counter, non-frozen collection, or static.

column_list
    Defines a partition and clustering columns, which affects how the data in stored.

    -   Compound primary key: the first column is the partition key, and the additional columns are clustering keys. Syntax: `PRIMARY KEY (partition_column_name, clustering_column_name [, ...])`
    -   Composite partition key: Multiple columns in the partition key. Enclose the partition key columns in parentheses. Syntax: `PRIMARY KEY ((partition_column_name[, ...]),clustering_column_name [, ...])`

table_options

CQL table properties and descriptions of the syntax.

Tunes data handling, including I/O operations, compression, and compaction. Table property options use the following syntax:

-   Single values: `option_name = 'value'`
-   Multiple values: `option_name = { 'subproperty' : 'value' [, ...] } [AND ...]`

    Simple JSON format, key-value pairs in a comma-separated list enclosed by curly brackets.


**Note:** When no value is specified, the default is used.

bloom_filter_fp_chance = N
    False-positive probability for SSTable bloom filter. When a client requests data, the bloom filter checks if the row exists before executing disk I/O. Values range from 0 to 1.0, where: `0` is the minimum value use to enable the largest possible bloom filter (uses the most memory) and `1.0` is the maximum value disabling the bloom filter.

    **Tip:** Recommended setting: `0.1`. A higher value yields diminishing returns.

    **Default**: `bloom_filter_fp_chance = '0.01'`

caching = { 'keys' : 'value', 'rows_per_partition' : 'value'}
    Optimizes the use of cache memory without manual tuning. Weighs the cached data by size and access frequency. Coordinate this setting with the global caching properties in the cassandra.yaml file. Valid values:

    -   `ALL`– all primary keys or rows
    -   `NONE`– no primary keys or rows
    -   `N`: (rows per partition only) – specify a whole number

    **Default**: `{ 'keys': 'ALL', 'rows_per_partition': 'NONE' }`

cdc
    Creates a Change Data Capture (CDC) log on the table.

    Valid values:

    -   `TRUE`- create CDC log
    -   `FALSE`- do not create CDC log

comments = 'some text that describes the table'
    Provide documentation on the table.

    **Tip:** Enter a description of the types of queries the table was designed to satisfy.

dclocal_read_repair_chance
    Probability that a successful read operation triggers a read repair, limited to the same datacenter as the coordinator node.

    **Warning:** This option is deprecated and should be set to `0.0`.

default_time_to_live
    TTL (Time To Live) in seconds, where zero is disabled. The maximum configurable value is `630720000` (20 years). Beginning in 2018, the expiration timestamp can exceed the maximum value supported by the storage engine; see the warning below. If the value is greater than zero, TTL is enabled for the entire table and an expiration timestamp is added to each column. A new TTL timestamp is calculated each time the data is updated and the row is removed after all the data expires.

    Default value: `0` (disabled).

    **Warning:** The database storage engine can only encode TTL timestamps through `January 19 2038 03:14:07 UTC` due to the Year 2038 problem. The TTL date overflow policy determines whether requests with expiration timestamps later than the maximum date are rejected or inserted. See -Dcassandra.expiration_date_overflow_policy.

gc_grace_seconds
    Seconds after data is marked with a tombstone (deletion marker) before it is eligible for garbage-collection. Default value: 864000 (10 days). The default value allows time for the database to maximize consistency prior to deletion.

    **Note:** Tombstoned records within the grace period are excluded from hints or batched mutations.

memtable_flush_period_in_ms
    Milliseconds before `memtables` associated with the table are flushed.

    When memtable_flush_period_in_ms=0, the memtable will flush when:

    -   the flush threshold is met
    -   on shutdown
    -   on nodetool flush
    -   when commitlogs get full

    **Default**: `0`

min_index_interval
    Minimum gap between index entries in the index summary. A lower min_index_interval means the index summary contains more entries from the index, which allows the database to search fewer index entries to execute a read. A larger index summary may also use more memory. The value for min_index_interval is the densest possible sampling of the index.

max_index_interval
    If the total memory usage of all index summaries reaches this value, DataStax Enterprise decreases the index summaries for the coldest SSTables to the maximum set by max_index_interval. The max_index_interval is the sparsest possible sampling in relation to memory pressure.

nodesync
    Manages the table repair settings using the following syntax:

    
    { 'enabled' : value, 'deadline_target_sec' : seconds }
    

    -   `enabled`: Set to `true` or `false` to enable/disable NodeSync on the table.

        Default: true.

    -   `deadline_target_sec`: Specify the maximum number of seconds to validate all segments of the table. Set to less than the gc_grace_seconds to avoid resurrecting deleted data. DataStax recommends using the nodetool nodesyncservice ratesimulator to calculate the appropriate setting.

        Default: Highest value of gc_grace_seconds or 4 days.


read_repair_chance
    The probability that a successful read operation triggers a read repair.

    **Warning:** This option is deprecated and should be set to `0.0`.

speculative_retry
    Configures rapid read protection. Normal read requests are sent to just enough replica nodes to satisfy the consistency level. In rapid read protection, extra read requests are sent to other replicas, even after the consistency level has been met. The speculative retry property specifies the trigger for these extra read requests.

    -   ALWAYS: The coordinator node sends extra read requests to all other replicas after every read of that table.
    -   Xpercentile: Track each table's typical read latency (in milliseconds). Coordinator node retrieves the typical latency time of the table being read and calculates X percent of that figure. The coordinator sends redundant read requests if the number of milliseconds it waits without responses exceeds that calculated figure.
    -   Nms: The coordinator node sends extra read requests to all other replicas if the coordinator node has not received any responses within `N` milliseconds.
    -   NONE: The coordinator node does not send extra read requests after any read of that table.

compression = { compression_map }

Configure the `compression_map` by specifying the compression algorithm `class` followed by the subproperties in simple JSON format.

**Tip:** Implement custom compression classes using the `org.apache.cassandra.io.compress.ICompressor` interface.

class
    Sets the compressor name. DataStax Enterprise provides the following built-in classes:

    -   `LZ4Compressor`
    -   `SnappyCompressor`
    -   `DeflateCompressor`

    **Important:** Use only compression implementations bundled with DSE.

    **Default**: `LZ4Compressor`.

chunk_length_in_kb
    Size (in KB) of the block. On disk, SSTables are compressed by block to allow random reads. Values larger than the default value might improve the compression rate, but increases the minimum size of data to be read from disk when a read occurs. The default value is a good middle ground for compressing tables. Adjust compression size to account for read/write access patterns (how much data is typically requested at once) and the average size of rows in the table.

    **Default**: `64`.

crc_check_chance
    When compression is enabled, each compressed block includes a checksum of that block for the purpose of detecting disk bit rot and avoiding the propagation of corruption to other replica. This option defines the probability with which those checksums are checked during read. By default they are always checked. Set to 0 to disable checksum checking and to 0.5, for instance, to check them on every other read.

    **Default**: `1.0`.

sstable_compression
    Disables compression. Specify a null value.

compaction = {compaction_map}

Construct a map of the compaction option and its subproperties.

Defines the strategy for cleaning up data after writes.

Syntax uses a simple JSON format:


compaction = { 
     'class' : 'compaction_strategy_name', 
     'property_name' : value [, ...] }


where the compaction_strategy_name is SizeTieredCompactionStrategy, TimeWindowCompactionStrategy, or LeveledCompactionStrategy.

**Important:** Use only compaction implementations bundled with DSE. See How is data maintained? for more details.

Common properties

The following properties apply to all compaction strategies.


compaction = { 
     'class' : 'compaction_strategy_name', 
     'enabled' : (true | false),
     'log_all' : (true | false), 
     'only_purge_repaired_tombstone' : (true | false), 
     'tombstone_threshold' : ratio,
     'tombstone_compaction_interval' : sec,
     'unchecked_tombstone_compaction' : (true | false),
     'min_threshold' : num_sstables,
     'max_threshold' : num_sstables }


enabled
    Enable background compaction.

    -   `true` runs minor compactions.
    -   `false` disables minor compactions.

    **Tip:** Use `nodetool enableautocompaction` to start running compactions.

    Default: `true`

log_all
    Activates advanced logging for the entire cluster.

    Default: `false`

only_purge_repaired_tombstone
    Enabling this property prevents data from resurrecting when repair is not run within the `gc_grace_seconds`. When its been a long time between repairs, the database keeps all tombstones.

    -   `true` - Only allow tombstone purges on repaired SSTables.
    -   `false` - Purge tombstones on SSTables during compaction even if the table has not been repaired.

    Default: `false`

tombstone_threshold
    The ratio of garbage-collectable tombstones to all contained columns. If the ratio exceeds this limit, compactions starts only on that table to purge the tombstones.

    Default: `0.2`

tombstone_compaction_interval
    Number of seconds before compaction can run on an SSTable after it is created. An SSTable is eligible for compaction when it exceeds the `tombstone_threshold`. Because it might not be possible to drop tombstones when doing a single SSTable compaction, and since the compaction is triggered base on an estimated tombstone ratio, this setting makes the minimum interval between two single SSTable compactions tunable to prevent an SSTable from being constantly re-compacted.

    Default: `86400` (1 day)

unchecked_tombstone_compaction
    Setting to `true` allows tombstone compaction to run without pre-checking which tables are eligible for the operation. Even without this pre-check, DSE checks an SSTable to make sure it is safe to drop tombstones.

    Default: `false`

min_threshold
    The minimum number of SSTables to trigger a minor compaction.

    **Restriction:** Not used in `LeveledCompactionStrategy`.

    Default: `4`

max_threshold
    The maximum number of SSTables before a minor compaction is triggered.

    **Restriction:** Not used in `LeveledCompactionStrategy`.

    Default: `32`

SizeTieredCompactionStrategy

The compaction class `SizeTieredCompactionStrategy` (STCS) triggers a minor compaction when table meets the `min_threshold`. Minor compactions do not involve all the tables in a keyspace. See SizeTieredCompactionStrategy (STCS).

**Note:** Default compaction strategy.

The following properties only apply to SizeTieredCompactionStrategy:


compaction = { 
     'class' : 'SizeTieredCompactionStrategy', 
     'bucket_high' : factor,
     'bucket_low' : factor, 
     'min_sstable_size' : int }


bucket_high
    Size-tiered compaction merges sets of SSTables that are approximately the same size. The database compares each SSTable size to the average of all SSTable sizes for this table on the node. It merges SSTables whose size in KB are within [average-size * bucket_low] and [average-size * bucket_high].

    Default: `1.5`

bucket_low
    Size-tiered compaction merges sets of SSTables that are approximately the same size. The database compares each SSTable size to the average of all SSTable sizes for this table on the node. It merges SSTables whose size in KB are within [average-size * bucket_low] and [average-size * bucket_high].

    Default: `0.5`

min_sstable_size
    STCS groups SSTables into buckets. The bucketing process groups SSTables that differ in size by less than 50%. This bucketing process is too fine-grained for small SSTables. If your SSTables are small, use this option to define a size threshold in MB below which all SSTables belong to one unique bucket.

    Default: `50` (MB)

**Note:** The `cold_reads_to_omit` property for SizeTieredCompactionStrategy (STCS) is no longer supported.

TimeWindowCompactionStrategy

The compaction class `TimeWindowCompactionStrategy` (TWCS) compacts SSTables using a series of *time windows* or *buckets*. TWCS creates a new time window within each successive time period. During the active time window, TWCS compacts all SSTables flushed from memory into larger SSTables using STCS. At the end of the time period, all of these SSTables are compacted into a single SSTable. Then the next time window starts and the process repeats. See TimeWindowCompactionStrategy (TWCS).

**Note:** All of the properties for STCS are also valid for TWCS.

The following properties apply only to TimeWindowCompactionStrategy:


compaction = { 
     'class' : 'TimeWindowCompactionStrategy, 
     'compaction_window_unit' : days,
     'compaction_window_size' : int, 
     'split_during_flush' : (true | false) }


compaction_window_unit
    Time unit used to define the bucket size. The value is based on the Java `TimeUnit`. For the list of valid values, see the Java API `TimeUnit` page located at https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html.

    Default: `days`

compaction_window_size
    Units per bucket.

    Default: `1`

split_during_flush
    Prevents mixing older data from repairs and hints with newer data from the current time window. During a flush operation, determines whether data partitions are split based on the configured time window.

    -   `false` - the data partitions are not split based on the configured time window.
    -   `true` - ensure that data repaired by NodeSync is placed in the correct TWCS window. Enable `split_during_flush` when using NodeSync with TWCS or when running node repairs.

    Default: `false`

    During the flush operation, the data is split into a maximum of 12 windows. Each window holds the data in a separate SSTable. If the current time is t0 and each window has a time duration of w, the data is split in the SSTables as follows:

    -   SSTable 0 contains data for the time period < t0 - 10 * w
    -   SSTables 1 to 10 contain data for the 10 equal time periods from (t0 - 10 * w) through to (t0 - 1 * w)
    -   SSTable 11, the 12th table, contains data for the time period > t0

LeveledCompactionStrategy

The compaction class `LeveledCompactionStrategy` (LCS) creates SSTables of a fixed, relatively small size (160 MB by default) that are grouped into levels. Within each level, SSTables are guaranteed to be non-overlapping. Each level (L0, L1, L2 and so on) is 10 times as large as the previous. Disk I/O is more uniform and predictable on higher than on lower levels as SSTables are continuously being compacted into progressively larger levels. At each level, row keys are merged into non-overlapping SSTables in the next level. See LeveledCompactionStrategy (LCS).

**Note:** For more guidance, see When to Use Leveled Compaction and Leveled Compaction blog.

The following properties only apply to LeveledCompactionStrategy:


compaction = { 
     'class' : 'LeveledCompactionStrategy, 
     'sstable_size_in_mb' : int }


sstable_size_in_mb
    The target size for SSTables that use the LeveledCompactionStrategy. Although SSTable sizes should be less or equal to sstable_size_in_mb, it is possible that compaction could produce a larger SSTable during compaction. This occurs when data for a given partition key is exceptionally large. The DSE database does not split the data into two SSTables.

    Default: `160`

DateTieredCompactionStrategy (deprecated)

**Important:** Use TimeWindowCompactionStrategy instead.

Stores data written within a certain period of time in the same SSTable.

base_time_seconds
    The size of the first time window.

    Default: `3600`

max_sstable_age_days (deprecated)
    DSE does not compact SSTables if its most recent data is older than this property. Fractional days can be set.

    Default: `1000`

max_window_size_seconds
    The maximum window size in seconds.

    Default: `86400`

timestamp_resolution
    Units, MICROSECONDS or MILLISECONDS, to match the timestamp of inserted data.

    Default: `MICROSECONDS`

Table keywords

CLUSTERING ORDER BY ( column_name ASC | DESC)
    Order rows storage to make use of the on-disk sorting of columns. Specifying order can make query results more efficient. Options are:

    `ASC`: ascending (default order)

    `DESC`: descending, reverse order

ID
    If a table is accidentally dropped with DROP TABLE, use this option to recreate the table and run a commit log replay to retrieve the data.

Examples

CREATE TABLE CQL examples.

Creating a table with UUID as the primary key

Create the `cyclist_name` table with UUID as the primary key:


CREATE TABLE IF NOT EXISTS cycling.cyclist_name (
  id UUID PRIMARY KEY,
  lastname text,
  firstname text
);


Creating a compound primary key

Create the `cyclist_category` table and store the data in reverse order:


CREATE TABLE IF NOT EXISTS cycling.cyclist_category (
  category text,
  points int,
  id UUID,
  lastname text,
  PRIMARY KEY (category, points)
)
WITH CLUSTERING ORDER BY (points DESC);


Creating a composite partition key

Create a table that is optimized for query by cyclist rank by year:


CREATE TABLE IF NOT EXISTS cycling.rank_by_year_and_name (
  race_year int,
  race_name text,
  cyclist_name text,
  rank int,
  PRIMARY KEY ((race_year, race_name), rank)
);


Creating a table with a vertex label or an edge label

Create the `person` table with a vertex label `person_label` as graph data:


CREATE TABLE IF NOT EXISTS food_cql.person ( 
   person_id UUID, 
   name text, 
   gender text,
   nickname set<text>,
   cal_goal int,
   macro_goal list<int>,
   badge map<text, date>,
   PRIMARY KEY (name, person_id)
) WITH CLUSTERING ORDER BY (person_id ASC) AND VERTEX LABEL person_label;


Create the `book` table with a vertex label `book_label` as graph data:


CREATE TABLE IF NOT EXISTS food_cql.book ( 
   book_id int, 
   name text,
   authors list<frozen<fullname>>,
   publish_year int,
   isbn text,
   category set<text>,
   PRIMARY KEY (name, book_id)
) WITH CLUSTERING ORDER BY (book_id ASC) AND VERTEX LABEL;


Create the `person_authored_book` table with an edge label `authored` as graph data:


CREATE TABLE IF NOT EXISTS food_cql.person_authored_book (
    person_id UUID,
    person_name text,
    book_id int,
    book_name text,
    PRIMARY KEY ( (person_name, person_id) , book_name, book_id)
) WITH EDGE LABEL person_authored_book
      FROM person(name, person_id)
      TO book(name, book_id);


See Managing Graphs for information on creating graphs.

Creating a table with a frozen UDT

Create the `race_winners` table that has a frozen user-defined type (UDT):


CREATE TABLE IF NOT EXISTS cycling.race_winners (
  cyclist_name FROZEN<fullname>, 
  race_name text,
  race_position int,
  PRIMARY KEY (race_name, race_position)
);


See Creating a user-defined type for information on creating UDTs. UDTs can be created unfrozen if only non-collection fields are used in the user-defined type creation. If the table is created with an unfrozen UDT, then individual field values can be updated and deleted.

Creating a table with a CDC log

Create a change data capture log for the `cyclist_id` table:


CREATE TABLE IF NOT EXISTS cycling.cyclist_id (
  lastname text,
  firstname text,
  age int,
  id UUID,
  PRIMARY KEY ((lastname, firstname), age)
);


CDC logging must be enabled in cassandra.yaml.

CAUTION:

Before enabling CDC logging, have a plan for moving and consuming the log information. After the disk space limit is reached, writes to CDC-enabled tables are rejected until more space is freed. See Change-data-capture (CDC) space settings for information about available CDC settings.

Storing data in descending order

The following example shows a table definition that stores the categories with the highest points first.


CREATE TABLE IF NOT EXISTS cycling.cyclist_category (
  category text,
  points int,
  id UUID,
  lastname text,
  PRIMARY KEY (category, points)
)
WITH CLUSTERING ORDER BY (points DESC);


Restoring from the table ID for commit log replay

Recreate a table with its original ID to facilitate restoring table data by replaying commit logs:


CREATE TABLE IF NOT EXISTS cycling.cyclist_emails (
  userid text PRIMARY KEY,
  id UUID,
  emails set<text>
)
WITH ID = '1bb7516e-b140-11e8-96f8-529269fb1459';


To retrieve a table's ID, query the `id` column of `system_schema.tables`. For example:


SELECT id
FROM system_schema.tables
WHERE keyspace_name = 'cycling'
  AND table_name = 'cyclist_emails';


To perform a point-in-time restoration of the table, see Restoring a backup to a specific point-in-time.


'''
