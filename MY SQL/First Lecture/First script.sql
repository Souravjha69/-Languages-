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

SELECT * from users; -- If mujhe pura table hi dekhna ho then ye wali command
SELECT ID from users;  -- If mujhe specifically ek hi column dekhna ho , command me then ye wali command
SELECT ID, Email from users; -- If mujhe specifically 2 command table me dekhni ho the ye wali command 
Rename table programmers to users; -- If i have to rename the table name the use this command
ALTER TABLE users DROP COLUMN created_by; -- If i want to delete any column then use this command here 
ALTER TABLE users ADD COLUMN created_at timestamp default current_timestamp; -- If i have to add any column in the table then use this command here
Alter table users add column is_active boolean default true; -- If i have to add any column in the table then use this command here
Select * from users;
