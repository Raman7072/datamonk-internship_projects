SELECT COUNT(*) AS february_payments
FROM payment
WHERE MONTH(payment_date) = 2;
