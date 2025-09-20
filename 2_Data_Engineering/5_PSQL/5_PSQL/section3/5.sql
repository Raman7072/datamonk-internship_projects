-- Enable FDW for PostgreSQL
CREATE EXTENSION IF NOT EXISTS postgres_fdw;

-- Connect to another database (example: billing DB)
CREATE SERVER billing_server
FOREIGN DATA WRAPPER postgres_fdw
OPTIONS (host 'localhost', dbname 'billing', port '5432');

CREATE USER MAPPING FOR current_user
SERVER billing_server
OPTIONS (user 'billing_user', password 'secret');

-- Import a table (e.g., payments)
IMPORT FOREIGN SCHEMA public
LIMIT TO (payments)
FROM SERVER billing_server
INTO public;

-- Join Sakila rental with billing payments
SELECT r.rental_id, r.customer_id, p.amount
FROM rental r
JOIN payments p ON r.rental_id = p.rental_id
LIMIT 10;
