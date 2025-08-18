SELECT last_name, COUNT(*) AS frequency
FROM actor
GROUP BY last_name
ORDER BY frequency DESC
LIMIT 5;
