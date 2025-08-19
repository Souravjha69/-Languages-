CREATE DATABASE Practice_mysql;
USE Practice_mysql;
CREATE TABLE users (
ID INT PRIMARY KEY auto_increment,
NAME varchar(200) not null,
Email varchar(200) not null,
Gender enum('Male', 'Female', 'Others') not null,
date_of_birth date,
created_by timestamp default current_timestamp
);

SELECT * from users;
SELECT ID from users;