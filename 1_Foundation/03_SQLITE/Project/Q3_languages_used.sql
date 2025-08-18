SELECT DISTINCT l.name AS language
FROM film f
JOIN language l ON f.language_id = l.language_id;
