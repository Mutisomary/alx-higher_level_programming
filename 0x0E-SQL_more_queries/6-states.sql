-- creates the database hbtn_0d_usa
-- create the table states on your MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	NAME VARCHAR(256) NOT NULL
);
