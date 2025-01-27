age = int(input("Taking Input Age: "))
if age >= 18:
    print("You're 18+")
elif age < 18:
    print("Your age is less than 18")
else:
    print(age)

#Traffice Problem 
# Traffic Light Problem 
light=input("Color of light is: -")
if light == "red":
    print("Stop the color is red")
elif light == "yellow":
    print("Look the color is yellow")
elif light == "green":
    print("You can go the color is green")
else:
    print("Light is broken")

#Grades of students Problem
marks=int(input("Enter the marks of the student : -"))
if marks>=90:
    print("You scored A grade")
elif marks>80 and marks<90:
    print("You scored B grade")
elif marks>70 and marks<80:
    print("You scored C grade")
else:
    print("You scored D grade FAIL")

# Print Output for
A = int(input("Enter the value of A: "))
G = input("M/F: ")

if (A == 1 or A == 2) and G == "M":
    print("fee is 100")
elif A == 3 or A == 4 or G == "F":
    print("fee is 200")
elif A == 5 and G == "M":
    print("fee is 300")
else:
    print("no fee")

# Single Line If / Ternary Operator
food=input("Enter the food:-")
eat="Yes It's Cake" if food=="Cake" else "no"
print(eat)

food2=input("Enter the second food2: -")
print("Sweet") if food2=="cake" or food2=="jalebi" else print("not sweet")

# Clever If / Ternary Operator
age=int(input("Enter the value of the age: -"))
vote=("No you don't have right to vote", "Yes you can vote")[age<=18] 
print(vote)

sal = float(input("Salary: "))
tax = sal * (0.2 if sal > 50000 else 0.1)
print("Tax:", tax)



