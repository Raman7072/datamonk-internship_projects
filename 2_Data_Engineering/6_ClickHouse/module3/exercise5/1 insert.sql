CREATE TABLE vector_test (id UInt32, value Float64)
ENGINE = MergeTree()
ORDER BY id;

INSERT INTO vector_test SELECT number, rand() FROM numbers(1000000);
