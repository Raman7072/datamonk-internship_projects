-- Enable extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Add a vector column for "film similarity"
ALTER TABLE film ADD COLUMN embedding vector(3);

-- Insert a mock embedding (you’d normally get this from an ML model)
UPDATE film SET embedding = '[0.1, 0.5, 0.3]'::vector WHERE film_id = 1;
UPDATE film SET embedding = '[0.2, 0.4, 0.7]'::vector WHERE film_id = 2;

-- Find nearest neighbor (cosine distance)
SELECT film_id, title, embedding <-> '[0.1, 0.5, 0.3]'::vector AS distance
FROM film
ORDER BY distance ASC
LIMIT 5;
