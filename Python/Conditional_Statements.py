age = int(input("Taking Input Age: "))
if age >= 18:
    print("You're 18+")
elif age < 18:
    print("Your age is less than 18")
else:
    print(age)


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