-- database stuff
-- create one
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- remove user
DROP USER IF EXISTS 'user_0d_2'@'localhost';
-- create user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grant select priv
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost'
