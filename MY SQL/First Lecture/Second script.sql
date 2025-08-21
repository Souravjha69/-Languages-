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

DROP database practice_mysql;


-- So this is the example so that i'll take multiple data in to one single query.
Insert into users (Name, gender, Email, date_of_birth) values
('Sourav 1', 'Male',  'sourav1@gmail.com', '1999-1-12'),
('Sourav 1', 'Male',  'sourav2@gmail.com', '1999-1-12'),
('Sourav 1', 'Male',  'sourav3@gmail.com', '1999-1-12'),
('Sourav 1', 'Male',  'sourav4@gmail.com', '1999-1-12'); 