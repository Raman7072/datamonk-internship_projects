-- Top 3 customers by total payments per country (using window functions)
WITH customer_pay AS (
  SELECT
    co.country,
    cust.customer_id,
    cust.first_name || ' ' || cust.last_name AS customer_name,
    COALESCE(SUM(p.amount), 0.0) AS total_payments
  FROM payment p
  JOIN rental r ON p.rental_id = r.rental_id
  JOIN customer cust ON r.customer_id = cust.customer_id
  JOIN address a ON cust.address_id = a.address_id
  JOIN city ci ON a.city_id = ci.city_id
  JOIN country co ON ci.country_id = co.country_id
  GROUP BY co.country, cust.customer_id, customer_name
)
SELECT country, customer_id, customer_name, total_payments
FROM (
  SELECT
    *,
    ROW_NUMBER() OVER (PARTITION BY country ORDER BY total_payments DESC) AS rn
  FROM customer_pay
) t
WHERE rn <= 3
ORDER BY country, total_payments DESC;
