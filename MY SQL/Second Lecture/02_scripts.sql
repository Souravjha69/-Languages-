USE  practice_sql;

-- Functions in the SQL Commands:-
SELECT COUNT(*) from users; -- Total number of users in the table Data.
SELECT COUNT(*) from users where gender = 'Male'; -- Total number of Men users in the Table Data.
SELECT COUNT(*) as Female_Count from  users where gender = 'Female'; -- Total number of Female users in the Table Data also Female count is column name only here.
SELECT MIN(salary) as MIN_SALARY , MAX(salary) as MAX_SALARY from users; -- Here watching the data what is minimum or max salary here from the users table and MIN_SALARY or MAX_SALARY is column name that I've created.

SELECT * FROM users Order by Salary ASC LIMIT 1 ; -- To see he lowest salary.
SELECT * FROM users Order by Salary DESC LIMIT 1; -- To see the highest salary.
SELECT SUM(salary) AS TOTAL_SALARY FROM users; -- To see the total salary from the users.
SELECT AVG(salary) AS AVG_SALARY FROM users; -- To see the Average Salary from the users.
SELECT gender, AVG(salary) AS AVG_SALARY FROM users GROUP BY gender;