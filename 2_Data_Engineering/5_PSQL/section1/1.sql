-- 1. Add a JSONB Column

-- Pick an existing table (say `products`) or create one:
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT,
    specs JSONB
);

-- Insert rows with different JSON shapes:
INSERT INTO products (name, specs)
VALUES
('Laptop', '{"cpu": "i7", "ram": "16GB", "extras": {"color": "black", "warranty": "2y"}}'),
('Phone', '{"screen": "6in", "battery": "4000mAh"}'),
('Headphones', '{"wireless": true, "noise_canceling": false}');

-- Query a specific key:
SELECT name, specs->>'cpu' AS cpu_model
FROM products
WHERE specs ? 'cpu';
