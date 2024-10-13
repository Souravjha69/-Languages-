#Practice Question
student={
    "name":"Sourav",
    "subjects":{
        "Math":85,
        "Eng":65,
        "Chem":45
    }
}

print(student.keys()) #Printing all the keys
print("Typecasting in the form of List",list(student.keys()))
print(len(list(student.keys())))
listStudents=list(student.keys()) #Storing the length of student in this variable 
print("Printing the ListStudents",listStudents)
print("Printing the len of these ",len(listStudents))

