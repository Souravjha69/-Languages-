USE Practice_mysql;
-- IN this script we are going to learn inserting data
Select * from users;

-- Here i have insterted the values as per the columns requirements and exact orders
Insert into users values
('1', 'Sourav kumar jha', 'Male', 'souravkumarjha301@gmail.com', '1999-10-03', Default, Default),
('4', 'Ritika Nath', 'Female', 'ritikanath78@gmail.com', '1996-05-03', Default, Default);




Insert into users (Name, gender, Email, date_of_birth) values
('Poorvi patil', 'Female', 'poorvi8@gmail.com', '1995-12-12'),
('Biplab', 'Male', 'biplab56@gmail.com', '1999-6-18');