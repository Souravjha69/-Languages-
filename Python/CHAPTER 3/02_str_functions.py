Myname= "Souravkumarjha"
Counting = Myname.count("")
Finding = Myname.find("a")
Replace = Myname.replace("Sourav", "Sunny")
print ("Length of my Full Name is like: -", (len(Myname)))
print ("Is jha is present in my Full Name?: - ", (Myname.endswith("jha"))) # Here it is checking my name is ending with jha or not so it returns boolean value True or false 
print ("Is Sourav name starts with my name: - ", (Myname.startswith("Sourav"))) # Here it is checking that my name is starting with "Sourav" or not so it returns boolean value True or false.
print ("It capitalize my first word like S only", (Myname.capitalize()))
print ("Count the entire character in the name: -", (Counting)) #Here it counts the entire character in the python string in Myname variable.
print ("Here the word a in my name is present at the index: -", (Finding)) # Here it finds the first occurrence of the letter "a" in my name and returns the index of that letter.
print ("Here I'm replacing the word SOurav with Sunny: -", (Replace)) # Here it replaces the word "Sourav" with "Sunny" in my name.
