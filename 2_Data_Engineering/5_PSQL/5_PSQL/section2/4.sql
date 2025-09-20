\copy jobs FROM 'jobs_large.csv' DELIMITER ',' CSV HEADER;


SELECT COUNT(*) FROM jobs;
