Myname= "Souravkumarjha"
Counting = Myname.count("")
Finding = Myname.find("a")
Replace = Myname.replace("Sourav", "Sunny")
print ("Length of my Full Name is like: -", (len(Myname)))
print ("Is jha is present in my Full Name?: - ", (Myname.endswith("jha"))) # Here it is checking my name is ending with jha or not so it returns boolean value True or false 
print ("Is Sourav name starts with my name: - ", (Myname.startswith("Sourav"))) # Here it is checking that my name is starting with "Sourav" or not so it returns boolean value True or false.
print ("It capitalize my first word like S only", (Myname.capitalize()))
print ("Count the entire character in the name: -", (Counting)) #Here it counts the entire character in the python string in Myname variable means index.
print ("Here the word a in my name is present at the index: -", (Finding)) # Here it finds the first occurrence of the letter "a" in my name and returns the index of that letter.
print ("Here I'm replacing the word SOurav with Sunny: -", (Replace)) # Here it replaces the word "Sourav" with "Sunny" in my name.

Sentence = "Sourav kumar jha is a good good boy."
Replacefirst = Sentence.replace("good", "bad", 1)
print ("Here I'm replacing the first occurence in this sentence rest are as there: -", (Replacefirst))


#Basic String Functions in Python: -
String1 = "Sourav"
Upper = String1.upper()
Lower = String1.lower()
print ("Uppercase of my name is like: -", (Upper)) # Here it converts the complete string to uppercase.
print ("Lower case of my name is like: -", (Lower)) # Here it converts the complete string to lowercase.
String2 = "Sourav kumar jha"
Tittle = String2.title()
print ("Tittle case of my name is like: - ", (Tittle)) # Here it converts the first letter of each word to uppercase and rest to lowercase.
String3 = "   Sourav kumar jha   "
Strip = String3.strip()
print ("Here is the original String3: - ",(String3)) #Original String3
print ("Remove the white space in String2 variable: -", (Strip))
String4 = "Swati jha is my sister"
find = String4.find("jha")
findr = String4.rfind("s",)
print ("Here I'm finding the word in this string: ", (find))
print ("Here I'm finidng the last occurence here: ",  (findr)) # Here it finds the last occurence of this word in the whole string and returns the index of that word.
String5 = "Swatis jha is really a good good girl"
Counting = String5.count("good")
print ("Here I'm finding how many time good word appears in the string: ", (Counting)) # So here it clarly counts word good how many times comes in this string. 
