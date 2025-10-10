INSERT INTO table_with_codec SELECT
    number,
    concat('user_', toString(number)),
    rand() / 100,
    now() - number
FROM numbers(1000000);




INSERT INTO table_without_codec SELECT
    number,
    concat('user_', toString(number)),
    rand() / 100,
    now() - number
FROM numbers(1000000);
