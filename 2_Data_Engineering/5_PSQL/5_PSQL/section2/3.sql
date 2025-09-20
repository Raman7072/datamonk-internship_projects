CREATE INDEX idx_people_city ON people(city);
CREATE INDEX idx_people_department ON people(department);


EXPLAIN ANALYZE
SELECT city, COUNT(*) 
FROM people
GROUP BY city;
