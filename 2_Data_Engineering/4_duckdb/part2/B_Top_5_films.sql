-- Top 5 films by total revenue (sum of customer_total_spend_for_film across distinct customers)
SELECT
  film_id,
  film_title,
  SUM(customer_total_spend_for_film) AS total_revenue
FROM 'sakila_insights.csv'
GROUP BY film_id, film_title
ORDER BY total_revenue DESC
LIMIT 5;
