-- user stuff
-- drop one
DROP USER IF EXISTS 'user_0d_1'@'localhost';
-- create one
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- give priv
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
