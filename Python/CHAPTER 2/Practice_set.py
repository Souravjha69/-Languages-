#Q1. Write a python program to add two numbers? 
a = 45
b = 78
print("Addition of a and b is like this: - ", a+b)

#Q2. Write a python program to find remainder when a number is divided by z? 
z= 10
h= 2
print("Here finding the remainder when a number is divided by z like this: - ", z%h)


#Q3. Check the type of variable assigned using input() function.
d = 78
e = "Sourav kumar jha"
f = 67.78

print ('Type of d variable is like: -', type(d))
print ("Type of e variable is like: -", type(e))
print ("Type of f variable is like: -", type(f))


#Q4. Use comparison operator to find out wheather a given variable a is greater than b or not. Take a = 34 and b = 80.
a =34
b = 80
if a > b:
    print("A is greater than B, B is less than A")
else:
    print("A is not greater than B, A is less than B") 

compareA = int(input("Enter the value of this: -"))
compareB = int(input("Enter the value of this: -"))

print("Here we are comparingt the value which is compareA is greater than compareB or not: -", compareA > compareB)


#Q5. Write a python program to find the average of two numbers entered by the user. 
NumberOne = int(input("Enter the first number:  "))
NumberTwo = int(input("Enter the second number:"))
AverageNumber = (NumberOne + NumberTwo)/2
print("Here this is the average number by taking the input from the user: ", int(AverageNumber)) #Here I'm putted int() function otherwise it will show the float value aalways default.

#Q6. Write a python program to calculate the square of a number entered by the user.
SquareNumberOne = int(input("Enter the numberone to find the square:"))
SquareNumberTwo = int(input("Enter the numbertwo to find the square:"))
SquareOne = SquareNumberOne * SquareNumberOne
print("Here this is the square value of both the numbers: ", SquareOne)