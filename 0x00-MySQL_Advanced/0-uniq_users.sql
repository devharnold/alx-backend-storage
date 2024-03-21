-- Script that creates a table `users`
-- `id` should be an integer, not null, auto increment, and a primary key
-- `email` string of 255 characters, not null and unique
-- `name` string 255 characters
-- if table exists script should not fail
-- can be executed on any database

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
