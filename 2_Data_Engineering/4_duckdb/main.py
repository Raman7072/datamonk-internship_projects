import duckdb
con = duckdb.connect()

# 1) preview CSV
print(con.execute("SELECT COUNT(*) FROM 'sakila_insights.csv'").fetchone())
print(con.execute("SELECT * FROM 'sakila_insights.csv' LIMIT 10").df())

# 2) top 5 films
print(con.execute("""
SELECT film_id, film_title, SUM(customer_total_spend_for_film) AS total_revenue
FROM 'sakila_insights.csv'
GROUP BY film_id, film_title
ORDER BY total_revenue DESC
LIMIT 5;
""").df())

# 3) unique customers
print(con.execute("""
SELECT category_name, COUNT(DISTINCT customer_id) AS unique_customers
FROM 'sakila_insights.csv'
GROUP BY category_name
ORDER BY unique_customers DESC;
""").df())

# 4) Action films
print(con.execute("""
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
ORDER BY s.customer_total_spend_for_film DESC
LIMIT 50;
""").df())

# 5) Histogram buckets
print(con.execute("""
SELECT
  CASE
    WHEN customer_total_spend_for_film < 10 THEN '< $10'
    WHEN customer_total_spend_for_film >= 10 AND customer_total_spend_for_film <= 50 THEN '$10 - $50'
    ELSE '> $50'
  END AS revenue_bucket,
  COUNT(*) AS customer_film_pairs
FROM 'sakila_insights.csv'
GROUP BY revenue_bucket
ORDER BY
  CASE revenue_bucket
    WHEN '< $10' THEN 1
    WHEN '$10 - $50' THEN 2
    ELSE 3
  END;
""").df())
