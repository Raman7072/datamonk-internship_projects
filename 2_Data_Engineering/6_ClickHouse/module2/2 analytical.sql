
-- PostgreSQL:
\timing
SELECT city, AVG(age) FROM people GROUP BY city;


-- ClickHouse
SELECT city, avg(age) FROM people GROUP BY city;
