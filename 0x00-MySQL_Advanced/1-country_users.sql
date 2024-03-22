-- Table `users`
-- `id` int, never null, auto increment, and primary key
-- `email` string(255), never null and unique
-- `name` string(255)
-- `country` enumeration (US, CO, TN)never null
-- if table exists, script should not fail

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
