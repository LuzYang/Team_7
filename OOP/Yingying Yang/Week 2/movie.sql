CREATE TABLE directors (
    id INTEGER PRIMARY KEY,  -- SQLite 自动递增
    name TEXT NOT NULL,
    nationality TEXT
);

CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    release_year INTEGER,
    director_id INTEGER,
    FOREIGN KEY (director_id) REFERENCES directors(id)ON DELETE CASCADE
);

INSERT INTO directors (name, nationality) VALUES
('Christopher Nolan', 'British-American'),
('Quentin Tarantino', 'American');

INSERT INTO movies (title, release_year, director_id) VALUES
('Inception', 2010, 1),
('Django Unchained', 2012, 2),
('Interstellar', 2014, 1);
SELECT movies.title, movies.release_year, directors.name AS director
FROM movies
JOIN directors ON movies.director_id = directors.id;
 