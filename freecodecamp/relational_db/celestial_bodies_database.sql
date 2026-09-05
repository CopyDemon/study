-- Connect back to postgres DB prevent still in universe DB and can't drop old DB
\c postgres;

-- Drop DB to create a new one
DROP DATABASE universe;

-- Create universe DB
CREATE DATABASE universe;

-- Connect to universe DB
\c universe;

-- Create tables
CREATE TABLE galaxy(
  galaxy_id INT NOT NULL PRIMARY KEY,
  name VARCHAR(20),
  radius INT,
  temperature INT,
  mass NUMERIC(4),
  description TEXT,
  fake_unique_column TEXT UNIQUE,
  liveable BOOLEAN NOT NULL
);


CREATE TABLE star(
  star_id INT NOT NULL PRIMARY KEY,
  galaxy_id INT NOT NULL,
  FOREIGN KEY (galaxy_id) REFERENCES galaxy(galaxy_id),
  name VARCHAR(20),
  radius INT,
  temperature INT,
  mass NUMERIC(4),
  description TEXT,
  fake_unique_column TEXT UNIQUE,
  liveable BOOLEAN NOT NULL
);


CREATE TABLE planet(
  planet_id INT NOT NULL PRIMARY KEY,
  star_id INT NOT NULL,
  name VARCHAR(20),
  radius INT,
  temperature INT,
  mass NUMERIC(4),
  description TEXT,
  liveable BOOLEAN NOT NULL,
  fake_unique_column TEXT UNIQUE,
  FOREIGN KEY (star_id) REFERENCES star(star_id)
);


CREATE TABLE moon(
  moon_id INT NOT NULL PRIMARY KEY,
  planet_id INT NOT NULL,
  name VARCHAR(20),
  radius INT,
  temperature INT,
  mass NUMERIC(4),
  description TEXT,
  liveable BOOLEAN NOT NULL,
  fake_unique_column TEXT UNIQUE,
  FOREIGN KEY (planet_id) REFERENCES planet(planet_id)
);

-- Placeholder table with placeholder_row, 
-- Task ask for 5 table and 3 row in each table, so just fake one lol
CREATE TABLE placeholder(
  placeholder_id INT PRIMARY KEY, 
  placeholder_content VARCHAR(100) NOT NULL, 
  fake_content BOOLEAN NOT NULL, 
  can_delete BOOLEAN,
  name VARCHAR(20),
  fake_unique_column TEXT UNIQUE
);


INSERT INTO galaxy 
(galaxy_id, name, radius, temperature, mass, description, liveable) 
VALUES 
(1, 'My galaxy', 10000, 24, 999, 'My first galaxy', true),
(2, 'My galaxy', 10000, 24, 999, 'My first galaxy', true),
(3, 'My galaxy', 10000, 24, 999, 'My first galaxy', true),
(4, 'My galaxy', 10000, 24, 999, 'My first galaxy', true),
(5, 'My galaxy', 10000, 24, 999, NULL, true),
(6, 'My galaxy', 10000, 24, 999, NULL, true);


INSERT INTO star 
(star_id, galaxy_id, name, radius, temperature, mass, description, liveable)
VALUES
(1, 1, 'Sun', '8876', 24, 9, 'This is Sun', true),
(2, 1, 'Sun', '8876', 24, 9, 'This is Sun', true),
(3, 1, 'Sun', '8876', 24, 9, 'This is Sun', true),
(4, 1, 'Sun', '8876', 24, 9, 'This is Sun', true),
(5, 1, 'Sun', '8876', 24, 9, NULL, true),
(6, 1, 'Sun', '8876', 24, 9, NULL, true);

INSERT INTO planet
(planet_id, star_id, name, radius, temperature, mass, description, liveable)
VALUES
(1, 1, 'Earth', 1000, 24, 1, 'This is Earth', true),
(2, 1, 'Earth', 1000, 24, 1, 'This is Earth', true),
(3, 1, 'Earth', 1000, 24, 1, 'This is Earth', true),
(4, 1, 'Earth', 1000, 24, 1, 'This is Earth', true),
(5, 1, 'Earth', 1000, 24, 1, 'This is Earth', true),
(6, 1, 'Earth', 1000, 24, 1, 'This is Earth', true),
(7, 1, 'Earth', 1000, 24, 1, 'This is Earth', true),
(8, 1, 'Earth', 1000, 24, 1, 'This is Earth', true),
(9, 1, 'Earth', 1000, 24, 1, 'This is Earth', true),
(10, 1, 'Earth', 1000, 24, 1, 'This is Earth', true),
(11, 1, 'Earth', 1000, 24, 1, NULL, true),
(12, 1, 'Earth', 1000, 24, 1, NULL, true);

INSERT INTO moon
(moon_id, planet_id, name, radius, temperature, mass, description, liveable)
VALUES
(1, 1, 'moon', 100, 4, 0.1, 'This is Earth', true),
(2, 1, 'moon', 100, 4, 0.1, 'This is Earth', true),
(3, 1, 'moon', 100, 4, 0.1, 'This is Earth', true),
(4, 1, 'moon', 100, 4, 0.1, 'This is Earth', true),
(5, 1, 'moon', 100, 4, 0.1, 'This is Earth', true),
(6, 1, 'moon', 100, 4, 0.1, 'This is Earth', true),
(7, 1, 'moon', 100, 4, 0.1, 'This is Earth', true),
(8, 1, 'moon', 100, 4, 0.1, 'This is Earth', true),
(9, 1, 'moon', 100, 4, 0.1, 'This is Earth', true),
(10, 1, 'moon', 100, 4, 0.1, 'This is Earth', true),
(11, 1, 'moon', 100, 4, 0.1, 'This is Earth', true),
(12, 1, 'moon', 100, 4, 0.1, 'This is Earth', true),
(13, 1, 'moon', 100, 4, 0.1, 'This is Earth', true),
(14, 1, 'moon', 100, 4, 0.1, 'This is Earth', true),
(15, 1, 'moon', 100, 4, 0.1, 'This is Earth', true),
(16, 1, 'moon', 100, 4, 0.1, 'This is Earth', true),
(17, 1, 'moon', 100, 4, 0.1, 'This is Earth', true),
(18, 1, 'moon', 100, 4, 0.1, 'This is Earth', true),
(19, 1, 'moon', 100, 4, 0.1, NULL, true),
(20, 1, 'moon', 100, 4, 0.1, NULL, true);

INSERT INTO placeholder
(placeholder_id, placeholder_content, fake_content)
VALUES
(1, 'Placeholder', true),
(2, 'Placeholder', true),
(3, 'Placeholder', true);
