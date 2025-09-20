-- 🔍 Fuzzy Search with pg_trgm

-- Enable extension
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- Find films with titles similar to "Jurrasic Pork"
SELECT title, similarity(title, 'Jurrasic Pork') AS score
FROM film
WHERE title % 'Jurrasic Pork'
ORDER BY score DESC
LIMIT 5;
