-- Here this is the practice session here: - 

-- This database I'm using right now: -
USE  starter_sql; 

SELECT * FROM users where salary > 60000 ORDER BY created_by DESC  LIMIT 5; -- In this list it is showing where i modified the data or entered the dats it sis showing in that form only.
SELECT * FROM users order by salary desc; -- In this list it is showing only salary is descending order also I'm filtering any data just I'm viewing the data in descending order so I've used here order.
SELECT * FROM users where Salary BETWEEN 50000 AND 70000; -- Here the salary is showing that lies in this value only.  
-- -----------------------
-- In this Command I'm updating the salary +10000 whose salary is less than 60000 here
SET SQL_SAFE_UPDATES = 0;
UPDATE users SET Salary = Salary + 10000 WHERE Salary < 60000;
SET SQL_SAFE_UPDATES = 1;
-- -----------------------
SELECT * FROM users where Salary > 60000.00;

SELECT ID, Name, Salary from users;

-- ---------------------------
-- Here I'm deleting the the user's data whose salary is less than 70000.
SET SQL_SAFE_UPDATES = 0;
DELETE FROM users where Salary < 70000.00;

-- Here I'm deleting the row data whose salary is NUll make sure you write is NUll not = NULL
Select * from users where Salary is Null;
DELETE FROM users where Salary is NULL;