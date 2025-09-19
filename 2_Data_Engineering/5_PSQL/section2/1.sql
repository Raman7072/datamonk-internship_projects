-- Step 1. Import people_large.csv into PostgreSQL


-- In psql
\copy people FROM 'people_large.csv' DELIMITER ',' CSV HEADER;


SELECT COUNT(*) FROM people;
