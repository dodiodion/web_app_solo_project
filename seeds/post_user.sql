DROP TABLE IF EXISTS users CASCADE;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name text,
    email text,
    username text,
    password text
);

DROP TABLE IF EXISTS posts CASCADE;

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    time_posted timestamp,
    content text,
    user_id int,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

INSERT INTO users (name, email, username, password) 
    VALUES ('Guest', 'bob@gmail.com', 'Guest', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92');

INSERT INTO users (name, email, username, password) 
    VALUES ('Bob Gratton', 'bob_gratton@hotmail.com', 'bob_gratton', 'ba28e715bb87f8126262007fd9651d3cae6a60faa48ccf8b62124b0fb7f6e01b');

INSERT INTO posts (time_posted, content, user_id)
    VALUES ('2021-12-09 15:45:21', 'There are pinguins on the beach', 1);

INSERT INTO posts (time_posted, content, user_id)
    VALUES ('2022-02-08 18:45:21', 'Am i really all the things that are outside of me', 2);

INSERT INTO posts (time_posted, content, user_id)
    VALUES ('2022-12-08 13:45:21', 'Smoking so much I cant breathe', 1);
