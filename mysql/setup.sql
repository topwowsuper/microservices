-- CREATE DATABASE IF NOT EXISTS animals;
USE animals;

CREATE TABLE animals ( id MEDIUMINT NOT NULL AUTO_INCREMENT, name CHAR(30) NOT NULL, PRIMARY KEY (id) );


INSERT INTO animals (name) VALUES
    ('dog'),('cat'),('penguin'),
    ('lax'),('whale'),('ostrich');

-- CREATE TABLE IF NOT EXISTS animals ( \
--      id MEDIUMINT NOT NULL AUTO_INCREMENT, \
--      name CHAR(30) NOT NULL, \
--      PRIMARY KEY (id) \
-- );

-- INSERT INTO animals (name) VALUES
--     ('dog'),('cat'),('penguin'),
--     ('lax'),('whale'),('ostrich');
-- CREATE TABLE IF NOT EXISTS (...);