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
);

-- This code helps when if you want to add column in  the table after creation of previous table or in modification of one column in the existing table.
ALTER TABLE users 
ADD COLUMN Salary VARCHAR(255),
ADD COLUMN Phone_Number varchar(15);

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

INSERT into users (name, Email, Gender, date_of_birth, created_by, Phone_Number) values
('Kapil Maurya', 'kapilmaurya789@gmail.com', 'Others', '2005-12-25', default, '+91 8298345566');

-- Here in this code if i want to update any column data like here I'm updating salary section in this data so
UPDATE users SET Salary = 75000.00 WHERE id = 1;
UPDATE users SET Salary = 65000.00 WHERE id = 2;
UPDATE users SET Salary = 82000.00 WHERE id = 3;
UPDATE users SET Salary = 75000.00 WHERE id = 4;
UPDATE users SET Salary = 65000.00 WHERE id = 5;
UPDATE users SET Salary = 82000.00 WHERE id = 6;
UPDATE users SET Salary = 75000.00 WHERE id = 7;
UPDATE users SET Salary = 65000.00 WHERE id = 8;
UPDATE users SET Salary = 82000.00 WHERE id = 9;
 UPDATE users SET Salary = 75000.00 WHERE id = 10;
UPDATE users SET Salary = 65000.00 WHERE id =11;
UPDATE users SET Salary = 82000.00 WHERE id = 12;
UPDATE users SET Salary = 75000.00 WHERE id = 13;
UPDATE users SET Salary = 65000.00 WHERE id = 14;
UPDATE users SET Salary = 82000.00 WHERE id = 15;
UPDATE users SET Salary = 75000.00 WHERE id = 16;
UPDATE users SET Salary = 65000.00 WHERE id = 17;
UPDATE users SET Salary = 85000.00 WHERE id = 18;
UPDATE users SET Phone_Number = '+91 8825142893' WHERE id = 1;

-- This code will help where i want to delete salary data in the table not column only data.
UPDATE users 
SET Salary = NULL 
WHERE id IN (1, 2, 3);

INSERT into users (ID, Name, Email, Gender, created_by)values
('17', 'Amruta Pawar', 'amruta78@gmail.com', 'Female', DEFAULT);