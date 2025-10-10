INSERT INTO codec_test_zstd SELECT concat('user_', toString(number)) FROM numbers(100000);
INSERT INTO codec_test_lz4 SELECT concat('user_', toString(number)) FROM numbers(100000);
