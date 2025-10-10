CREATE TABLE table_without_codec
(
    id UInt32,
    name String,
    value Float32,
    created_at DateTime
)
ENGINE = MergeTree()
ORDER BY id;
