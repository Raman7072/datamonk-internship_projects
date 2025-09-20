-- 4. Model Booking Windows with Range Types

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    guest TEXT,
    stay DATERANGE
);

INSERT INTO bookings (guest, stay)
VALUES
('Alice', '[2025-01-10,2025-01-15)'),
('Bob', '[2025-01-12,2025-01-18)'),
('Charlie', '[2025-02-01,2025-02-05)');

-- Find bookings overlapping Jan 13 to Jan 14
SELECT guest, stay
FROM bookings
WHERE stay && '[2025-01-13,2025-01-14)';
