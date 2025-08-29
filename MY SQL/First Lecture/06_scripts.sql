-- This script we are using for delete and others queries: -
SELECT * FROM users;

INSERT into users (ID, Name, Email, Gender, date_of_birth, created_by, Salary, Phone_Number) values
('18', 'Sahil Khan', 'sahil@example.com', 'Male', '2003-12-21', DEFAULT, '89000', '+91 987645988');

SELECT * FROM users where ID = '18';

-- This is Update command.
UPDATE users set Salary = '90,000.00' where ID = '18';

-- Delete Command here
DELETE FROM users where ID = '18'; -- Delete Salary specifically where id is 18.
DELETE FROM users where Name = 'Sahil Khan' -- Delete salary where specifically name = 'Sahil khan'.