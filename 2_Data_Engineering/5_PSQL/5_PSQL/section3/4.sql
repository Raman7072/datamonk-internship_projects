-- Enable extension
CREATE EXTENSION IF NOT EXISTS timescaledb;

-- Convert rental into hypertable
SELECT create_hypertable('rental', 'rental_date', if_not_exists => TRUE);

-- Example: rentals grouped by week
SELECT time_bucket('1 week', rental_date) AS week,
       COUNT(*) AS rentals
FROM rental
GROUP BY week
ORDER BY week;
