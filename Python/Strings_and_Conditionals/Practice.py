name=input("Enter your name: ")
print(name)
print("Length of the string Name",len(name))

#Find the occurence of $
name2="Sourav$ kr$ jha$"
print("Printing the count/Occurence",name2.count("$"))

#Conditional Practice
Marks=int(input("Enter the marks: "))
if Marks>=90:
    print("You obtained a Grade A")
elif Marks>=80 or Marks<90:
    print("You obtained a Grade B")
elif Marks>70 or Marks<80:
    print("You obtained a Grade C")
elif Marks>60 or Marks<70:
    print("You obtained a Grade D")

print("Your grade will be rewarded as: ", Marks)


#Nesting
DrivingAge=int(input("Enter Your Age:"))
if DrivingAge>=18:
    if DrivingAge>=55:
        print("You have also not the valid age for Driving here.")
else:
    print("You have not valid age for Driving")