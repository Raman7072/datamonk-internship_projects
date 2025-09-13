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
