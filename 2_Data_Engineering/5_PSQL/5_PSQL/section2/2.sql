-- Group by city
EXPLAIN ANALYZE
SELECT city, COUNT(*) 
FROM people
GROUP BY city;

-- Group by department
EXPLAIN ANALYZE
SELECT department, AVG(salary) 
FROM people
GROUP BY department;


