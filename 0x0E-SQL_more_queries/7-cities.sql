-- my the force be with you
-- create db
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use it
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS cities (
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
state_id INT NOT NULL,
FOREIGN KEY (state_id) REFERENCES states(id),
name VARCHAR(256) NOT NULL
)
