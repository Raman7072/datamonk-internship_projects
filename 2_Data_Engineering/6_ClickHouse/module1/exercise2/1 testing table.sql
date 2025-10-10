CREATE TABLE codec_test_zstd
(
    name String CODEC(ZSTD)
)
ENGINE = MergeTree()
ORDER BY tuple();

CREATE TABLE codec_test_lz4
(
    name String CODEC(LZ4)
)
ENGINE = MergeTree()
ORDER BY tuple();
