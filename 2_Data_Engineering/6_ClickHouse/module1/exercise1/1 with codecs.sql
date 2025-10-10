CREATE TABLE table_with_codec
(
    id UInt32,
    name String CODEC(ZSTD),
    value Float32 CODEC(DoubleDelta),
    created_at DateTime CODEC(Delta, ZSTD)
)
ENGINE = MergeTree()
ORDER BY id;
