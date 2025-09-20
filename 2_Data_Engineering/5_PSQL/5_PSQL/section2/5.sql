EXPLAIN ANALYZE
SELECT p.first_name, p.last_name, j.salary
FROM people p
JOIN jobs j
  ON p.person_id = j.person_id;


CREATE INDEX idx_jobs_person_id ON jobs(person_id);
