-- creates the database hbtn_0d_usa
-- create the table states on your MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT AUTO INCREMENT PRIMARY KEY NOT NULL,
	NAME VARCHAR(256) NOT NULL
);
