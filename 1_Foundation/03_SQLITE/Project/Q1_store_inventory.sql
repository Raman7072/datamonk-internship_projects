SELECT s.store_id, COUNT(i.inventory_id) AS total_films
FROM store s
JOIN inventory i ON s.store_id = i.store_id
GROUP BY s.store_id;
