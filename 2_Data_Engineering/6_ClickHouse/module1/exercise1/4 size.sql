SELECT table, sum(bytes) AS total_size_bytes
FROM system.parts
WHERE table IN ('table_with_codec', 'table_without_codec')
GROUP BY table;
