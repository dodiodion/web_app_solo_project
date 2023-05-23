DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS artists_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text,
    genre text
);

INSERT INTO artists (name, genre) VALUES ('Pixies', 'Indie');
INSERT INTO artists (name, genre) VALUES ('ABBA', 'Disco');
INSERT INTO artists (name, genre) VALUES ('Taylor Swift', 'Modern Country');
INSERT INTO artists (name, genre) VALUES ('Nina Simone', 'Jazz');