-- 3. Work with hstore

CREATE EXTENSION IF NOT EXISTS hstore;

CREATE TABLE user_prefs (
    id SERIAL PRIMARY KEY,
    username TEXT,
    prefs HSTORE
);

INSERT INTO user_prefs (username, prefs)
VALUES
('alice', 'theme=>"dark", language=>"en"'),
('bob', 'theme=>"light", language=>"fr"');

SELECT username, prefs->'language' AS language_pref
FROM user_prefs;
