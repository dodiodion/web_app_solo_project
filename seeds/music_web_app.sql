
DROP TABLE IF EXISTS artists CASCADE;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text,
    genre text
);

DROP TABLE IF EXISTS albums CASCADE;

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int,
    constraint fk_artist foreign key(artist_id)
    references artists(id)
    on delete cascade
);

INSERT INTO artists (name, genre) VALUES ('MGMT', 'Indie Rock');
INSERT INTO artists (name, genre) VALUES ('Tyler the Creator', 'Rap');

INSERT INTO albums (title, release_year, artist_id) VALUES ('Getter Album', 2004 , 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Congratulations', 2010 , 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('IGOR', 2019 , 2);
