SELECT COUNT(*) AS february_payments
FROM payment
WHERE strftime('%m', payment_date) = '02';
