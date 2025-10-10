CREATE TABLE replacing_test
(
    id UInt32,
    name String,
    version UInt32
)
ENGINE = ReplacingMergeTree(version)
ORDER BY id;
