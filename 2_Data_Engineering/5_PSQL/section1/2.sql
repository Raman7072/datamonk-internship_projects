-- 2. Use citext for Emails

-- Enable the extension:
CREATE EXTENSION IF NOT EXISTS citext;

-- Create a table with case-insensitive email:
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email CITEXT UNIQUE
);

-- Test inserts:
INSERT INTO users (email) VALUES ('Test@Example.com');
INSERT INTO users (email) VALUES ('test@example.com');  -- will fail because CITEXT treats them as equal
