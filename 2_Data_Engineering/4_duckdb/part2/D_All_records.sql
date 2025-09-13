WITH cat_avg AS (
  SELECT category_name, AVG(customer_total_spend_for_film) AS avg_spend
  FROM 'sakila_insights.csv'
  GROUP BY category_name
)
SELECT s.*
FROM 'sakila_insights.csv' s
JOIN cat_avg ca ON s.category_name = ca.category_name
WHERE s.category_name = 'Action'
  AND s.customer_total_spend_for_film > ca.avg_spend
ORDER BY s.customer_total_spend_for_film DESC;
