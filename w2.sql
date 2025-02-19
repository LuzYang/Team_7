-- Create Authors Table
CREATE TABLE Authors (
    author_id INTEGER PRIMARY KEY,  
    name TEXT,                
    birthdate TEXT,  -- Using TEXT for DATE format (YYYY-MM-DD)
    nationality TEXT                   
);

-- Insert into Authors Table
INSERT INTO Authors (author_id, name, birthdate, nationality) 
VALUES 
    (12, 'koiri', '2000-09-10', 'Indian'),
    (13, 'susan', '2000-09-10', 'Italian'),
    (14, 'mula', '2000-09-10', 'Kosovoich');

-- Create Books Table
CREATE TABLE Books (
    bookid INTEGER PRIMARY KEY,    
    title TEXT,             
    author_id INTEGER,                            
    genre TEXT,                       
    publication_year INTEGER,                      
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)  
);

-- Insert into Books Table
INSERT INTO Books (title, author_id, genre, publication_year) 
VALUES 
    ('Games of Thrones', 12, 'Poem', 1990),
    ('Mula Ko Saag', 13, 'Fairytale', 1890),
    ('Pani Ma Dhunga', 14, 'Lovestory', 1989);

-- Retrieve all records from Authors table
SELECT * FROM Authors;
-- Retrieve all records from Books table
SELECT * FROM Books;
