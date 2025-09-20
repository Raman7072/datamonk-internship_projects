-- Enable extension
CREATE EXTENSION IF NOT EXISTS pg_cron;

-- Schedule nightly cleanup of expired rentals
SELECT cron.schedule(
    'nightly_rental_cleanup',
    '0 2 * * *',  -- every day at 2 AM
    $$ DELETE FROM rental WHERE return_date < NOW() - INTERVAL '1 year'; $$
);
