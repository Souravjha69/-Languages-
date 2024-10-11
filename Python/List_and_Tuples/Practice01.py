#Print 3 movies and store them into the array
Movies=[]
Mov1=input("Enter the Movie 1: ")
Mov2=input("Enter the Movie 2: ")
Mov3=input("Enter the Movie 3: ")

Movies.append(Mov1)
Movies.append(Mov2)
Movies.append(Mov3)

print(Movies)

#Check Palindrome or not  
list = [1, 2, 1]
list2 = list.copy()  # Make a copy of the original list
list2.reverse()  # Reverse the copy

if list == list2:  # Compare the original list with the reversed copy
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

#Count the no. of students
Grade=["C", "D", "A", "A", "B", "B", "A"]
print("Count of A Grade", Grade.count("A"))

#Sort the A to D
grade =["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade) #In a ascending order
