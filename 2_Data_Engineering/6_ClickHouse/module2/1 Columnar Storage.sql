
-- PostgreSQL:
\copy people FROM '/path/to/people.csv' CSV HEADER;
SELECT count(*) FROM people;



-- ClickHouse:
CREATE TABLE people
(
    id UInt32,
    first_name String,
    last_name String,
    age UInt8,
    city String
)
ENGINE = MergeTree()
ORDER BY id;

INSERT INTO people SELECT number, 'Name_' || toString(number), 'Surname', rand()%100, 'City' FROM numbers(1000000);
SELECT count(*) FROM people;
