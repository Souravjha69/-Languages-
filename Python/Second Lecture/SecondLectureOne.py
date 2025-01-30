#Conditional Statements
age = int(input("Enter your age here:- "))
AgeMem = age
if(AgeMem >= 18):
    print("Yes you are valid member to drive.")
else:
    print("You are not a valid member here")



#Second Example
Light= input("Enter the color of the light:- ")

if(Light == "Green"):
    print("Yes you are free to go")
elif(Light == "Yellow"):
    print("You can drive slowly")
elif(Light == "Red"):
    print("You have to stop at this signal here.")
else:
    print("Light is broken")


# The difference between if and elif here is like if statement check many time and if statements true then it will check other condition, but in the case of elif if condition is not then
# it will check other conditions  only one time 


# Third Example
Marks =int(input("Enter the Marks of the student:- "))
if(Marks>=90):
    print("You got A Grade")
elif(Marks>=80):
    print("You got B Grade")
elif(Marks>=60):
    print("You got only C Grade")
else:
    print("You got D grade here")