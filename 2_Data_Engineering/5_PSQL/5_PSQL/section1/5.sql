-- 5. Build a Materialized View for Analytics


SELECT c.customer_id, c.first_name, COUNT(r.rental_id) AS rentals
FROM customers c
JOIN rentals r ON c.customer_id = r.customer_id
GROUP BY c.customer_id, c.first_name;


CREATE MATERIALIZED VIEW mv_customer_rentals AS
SELECT c.customer_id, c.first_name, COUNT(r.rental_id) AS rentals
FROM customers c
JOIN rentals r ON c.customer_id = r.customer_id
GROUP BY c.customer_id, c.first_name;


SELECT * FROM mv_customer_rentals;


REFRESH MATERIALIZED VIEW mv_customer_rentals;
