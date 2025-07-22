#Arithmetic Operators
a = 10
b = 20
print("This is a variable:", (a + b))

#Assignment Operators
a= 78-34
print("This is the example of assignment operator:", a)
b= 6
b+= 45
print("Here we increment the value of b:", b)
b-= 10
print("Here we decrement the value of b:", b)

#Comparison Operators
d = 10>5
print("This is the example of comparison operator:", d)
e = 8>=8
print("This is the example of comparison operator:", e) #Here either it checks it equal or greater than
f= 5!=5 #Actually here it says 5 is not equal to 5 but it's equal so it returns false 
print("This is the example of comparison operator:", f) #Here it checks if the two values are not equal
g =10!= 5
print("This is the example of comparison operator:", g) #Here it checks if the two values are not equal
h= 7==7
print("This is the example of comparison operator:", h) #Here it checks if the two values are equal
#Here comparison operators either return True or False

#Logical Operators
lining = True or True
print("This is the example of logical operator:", lining) #Here it checks if either of the two values is True means any one value returns True then its True
lining2 = True and False
print("This is the example of logical operator:", lining2) #Here it checks if both values are True then it returns True otherwise False
#Truth Table for Logical Operators:
#Truth table of {OR}
print("True or True:", True or True)  # True
print("True or False:", True or False)  # True
print("False or True:", False or True)  # True  
print("False or False:", False or False)  # False
#Truth table of {AND}
print("True and True:", True and True)  # True
print("True and False:", True and False)  # False
print("False and True:", False and True)  # False
print("False and False:", False and False)  # False
