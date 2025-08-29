-- Here I've created a Database: -
CREATE DATABASE practice_sql;
-- --------------------------------------------

-- Here I've used that Database: -
USE  practice_sql;
-- --------------------------------------------

-- Here I've created the table Users in the database:-
CREATE TABLE users (
ID INT PRIMARY KEY auto_increment,
Name VARCHAR(150),
Email VARCHAR(250) UNIQUE NOT NULL,
Salary varchar(250),
Gender enum('Male','Female','Other'),
Phone_No varchar(80) NOT NULL,
Created_by timestamp default current_timestamp
);

-- --------------------------------------------

-- Here I'm watching that data the table I've created 
Select * from users;

-- --------------------------------------------
-- Here I'm inserting the data in the table: -
INSERT into users ( Name, Email, Salary, Gender, Phone_No, Created_by)values
('Sourav kumar jha', 'souravkumarjha301@gmail.com', '95000.00', 'Male', '8825142893', DEFAULT),
('Anjali Sharma', 'anjali.sharma@example.com', 65000.00, 'Female', '9876543210', DEFAULT),
('Rohan Mehta', 'rohan.mehta@example.com', 82000.00, 'Male', '9123456780', DEFAULT),
('Priya Verma', 'priya.verma@example.com', 72000.00, 'Female', '9988776655', DEFAULT),
('Amit Kumar', 'amit.kumar@example.com', 90000.00, 'Male', '8899776655', DEFAULT),
('Neha Gupta', 'neha.gupta@example.com', 61000.00, 'Female', '7766554433', DEFAULT),
('Arjun Singh', 'arjun.singh@example.com', 85000.00, 'Male', '7001122334', DEFAULT),
('Sneha Roy', 'sneha.roy@example.com', 58000.00, 'Female', '7896541230', DEFAULT),
('Vikram Yadav', 'vikram.yadav@example.com', 77000.00, 'Male', '9345678123', DEFAULT),
('Meera Iyer', 'meera.iyer@example.com', 69000.00, 'Female', '9567812340', DEFAULT),
('Karan Malhotra', 'karan.malhotra@example.com', 88000.00, 'Male', '9123987654', DEFAULT);


UPDATE users set Name = 'Sarika Gosh' where id = '8'; 