USE  starter_sql;

-- Quering the data from the users:-
SELECT Name, Email from users; -- Here I'm checking specific data from the users only name and email ID
SELECT * FROM users WHERE gender = 'Female'; -- Here I'm putting the condition where gender is only females I'm checking in the users data. 

-- Here I'm watching the data with different conditions : -
SELECT * FROM users WHERE gender = 'Male'; -- Here I'm putting the condition where gender is only males I'm checking in the users data.
SELECT * FROM users WHERE gender <> 'Male'; -- Here I'm checking the female data in the users where geneder is not equal to male.
SELECT * FROM users WHERE gender != 'Male'; -- Here I'm checking the female data in the users where geneder is not equal to male.
SELECT * FROM users where date_of_birth < '1999-03-10'; -- So in this query I'm checking the data whose less only this date month year.
SELECT * FROM users where ID >= 10; -- So in this query I'm checking where Id is greater also equal than 10.
SELECT * FROM users where date_of_birth is NULL;  -- Here I'm checking the data where data is equal null only in the users table
SELECT * FROM users where Phone_Number is NOT NULL; -- Here I'm checking that whose phone number is null in the user data.
SELECT * FROM users where date_of_birth is NOT NULL;  -- Here I'm checking the data where data is not null only in the users table
SELECT * FROM users where date_of_birth between '1995-01-01' AND '2000-12-30'; -- Here the data is showing only where it lies between these year only
SELECT * from users where salary between '20000 ' and '80000'; -- Here the data is showing only where it lies between these salary only.
SELECT * FROM users where gender in ('Male', 'Female'); -- Here in this data i am finding where the value is male and female that value returns.
SELECT * FROM users where gender in ('Others'); -- Here in this data i'm finding where the value is others returns in gender column.
SELECT * From users where gender = "Male" and salary > "70000"; -- Here in this code it returns male data whose salary is above 70000 by and method.
SELECT * From users where gender = "Male" or salary > '80000'; -- Here in this satisfy atleast one data is also okay that will be shown like females also
SELECT * FROM users where gender = 'Male' or salary > '75000' ORDER BY date_of_birth ASC; -- In this data atleast satisy one condition but data shown in ascending order by Date of birth means big to small.
SELECT * FROM users where gender = 'Male' or salary > '78000' ORDER BY date_of_birth DESC LIMIT 5; -- In this data atleast satisy one condition but data shown in ascending order by Date of birth means small to big and shown in the limit 5 only means only 5 data will shown here.