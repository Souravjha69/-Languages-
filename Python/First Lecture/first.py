print("Hello world")


print ("Sourav is my name, My age is 24.")

# Charset here I'm printing
print(23)
# Printing the sum of the numbers
print(435+6545) 

# Variables and inside their values 
firstvar = 54
print(firstvar)
# Changing the value
firstvar = 44
print(firstvar)

# This is the string
Name2= "Sourav kumar jha"
# Here right side value is going to be stored in right side

# This is the example of that
name= "Sourav kumar jha" 
Age=24
price=25.9

print("My name is",name)
print("My age is",Age)
print("This product price is like", price)


# Here this is the example of assigning of one variable of another variable value directly
Age2= Age
print("Now here's the value if Age2 is",Age2)

# Now here I'm printing the type of Variable 
print(type(name))
print(type(Age))
print(type(price))


# Arithmetic Operators Examples
a= 24
b= 45

print("The sum of two no. will be", a+b)
print("The subtraction of two no. will be", a-b)
print("The multiplication of two no. will be", a*b) 
print("The division of two no. will be", a/b)
print("The remainder finding between these number wil be", a%b)


# Examples of Relation al Operators
d=65
e=67

print("Is d is equal to e", d==e) #False
print("Here d is not equal to e", d!=e) #True
print("Is d is greater than e", d>e) #False
print("Is d is smaller than equal to e", d<=e)

# Examples of Assignment Operators
num=40 
num=num+40 #num+=40 same both works equal
print("Then final value of num will be", num) #80 will be the answer

num2=20
num2 **=2 # This will be become my power operator. 
print(num2)

# Examples of Logical Operators
num3=44
num4=55
print(not(num3>num4)) #Whatever the output will return true or false not will give you the opposite of the output.

print("Example of and operator will be", (num3<num4)and (num3<num4)) #In this the rquirement it returns True only when both the conditions are True otherwise it will return False.
print("Example of or operator will be", (num3<num4)or(num3>num4))  #In this statement answer will return True because in or operator either in both conditions any on condition is True then it will return True.

#Examples of Type Conversions
news=55
news2=55.5
sumNews=news+news2
print("The value of sumNews",sumNews) #This is the example of Changing Type of Variables.

news3=int("58")
print(type(news3)) #Now this is the example of type casting here it's changed string type of integer type.


# Taking input from the User
Inputs= input("Enter Your name:")
print(Inputs)

change= input("Enter your Integer Number: -")
change2=int(change)
print(type(change2)) #Here I changed the input string to integer type.
