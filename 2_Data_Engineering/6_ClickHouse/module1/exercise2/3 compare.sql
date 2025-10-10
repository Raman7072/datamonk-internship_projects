SELECT table, sum(bytes) AS total_size_bytes
FROM system.parts
WHERE table LIKE 'codec_test_%'
GROUP BY table;
