COPY (
  WITH
  film_cat AS (
    SELECT
      f.film_id,
      f.title AS film_title,
      c.name AS category_name
    FROM film f
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
  ),
  inv AS (
    SELECT i.inventory_id, i.film_id, i.store_id
    FROM inventory i
  ),
  store_loc AS (
    SELECT s.store_id, a.address, ci.city, co.country
    FROM store s
    JOIN address a ON s.address_id = a.address_id
    JOIN city ci ON a.city_id = ci.city_id
    JOIN country co ON ci.country_id = co.country_id
  ),
  rental_pay AS (
    SELECT r.rental_id, r.inventory_id, r.customer_id, r.rental_date, p.payment_id, p.amount, p.payment_date
    FROM rental r
    LEFT JOIN payment p ON r.rental_id = p.rental_id
  )
  SELECT
    fcat.film_id,
    fcat.film_title,
    fcat.category_name,
    cust.customer_id,
    cust.first_name || ' ' || cust.last_name AS customer_name,
    sl.city AS store_city,
    sl.country AS store_country,
    rp.rental_date,
    (
      SELECT COALESCE(SUM(p2.amount), 0.0)
      FROM payment p2
      JOIN rental r2 ON p2.rental_id = r2.rental_id
      JOIN inventory i2 ON r2.inventory_id = i2.inventory_id
      WHERE i2.film_id = fcat.film_id
        AND r2.customer_id = cust.customer_id
    ) AS customer_total_spend_for_film
  FROM rental_pay rp
  JOIN inv i ON rp.inventory_id = i.inventory_id
  JOIN film_cat fcat ON i.film_id = fcat.film_id
  JOIN customer cust ON rp.customer_id = cust.customer_id
  LEFT JOIN store_loc sl ON i.store_id = sl.store_id
  WHERE rp.rental_date IS NOT NULL
) TO 'sakila_insights.csv' (HEADER, DELIMITER ',');
