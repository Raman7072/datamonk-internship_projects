SELECT category_name,
    COUNT(DISTINCT customer_id) AS unique_customers
FROM 'sakila_insights.csv'
GROUP BY category_name
ORDER BY unique_customers DESC;
