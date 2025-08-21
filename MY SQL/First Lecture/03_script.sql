CREATE DATABASE starter_sql;  -- This is the code of creating entire database here
USE  starter_sql;   -- This is the database of using the new database


-- Data creation
CREATE TABLE users(
ID INT PRIMARY KEY AUTO_INCREMENT,
Name Varchar(200),
Email Varchar(200) Unique not null,
Gender Enum('Male', 'Female', 'Others') not null,
date_of_birth date,
created_by timestamp default current_timestamp
)

-- This code defines to watch my code
SELECT * from users;

-- Now Data Insertion here : -
INSERT into users (name, Email, Gender, date_of_birth, created_by) values
('Sourav kumar jha', 'souravkumarjha301@gmail.com', 'Male', '1999-10-03', default),
('Anjali Sharma', 'anjali.sharma@example.com', 'Female', '2000-05-12', DEFAULT),
('Rohan Mehta', 'rohan.mehta@example.com', 'Male', '1998-09-21', DEFAULT),
('Priya Verma', 'priya.verma@example.com', 'Female', '1997-03-15', DEFAULT),
('Amit Kumar', 'amit.kumar@example.com', 'Male', '1996-11-30', DEFAULT),
('Neha Gupta', 'neha.gupta@example.com', 'Female', '2001-07-25', DEFAULT),
('Arjun Singh', 'arjun.singh@example.com', 'Male', '1999-01-10', DEFAULT),
('Sneha Roy', 'sneha.roy@example.com', 'Female', '1995-04-18', DEFAULT),
('Vikram Yadav', 'vikram.yadav@example.com', 'Male', '2002-06-05', DEFAULT),
('Meera Iyer', 'meera.iyer@example.com', 'Female', '1998-12-09', DEFAULT),
('Karan Malhotra', 'karan.malhotra@example.com', 'Male', '1997-08-22', DEFAULT),
('Simran Kaur', 'simran.kaur@example.com', 'Female', '1996-02-14', DEFAULT),
('Aditya Nair', 'aditya.nair@example.com', 'Male', '1995-09-07', DEFAULT),
('Pooja Reddy', 'pooja.reddy@example.com', 'Female', '2000-11-19', DEFAULT),
('Rahul Choudhary', 'rahul.choudhary@example.com', 'Male', '1999-03-28', DEFAULT),
('Shivani Mishra', 'shivani.mishra@example.com', 'Female', '1998-07-16', DEFAULT); 