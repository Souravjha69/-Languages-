str1= "Sourav"
print(len(str1))
length= len(str1)
print(length)
print(type(length))


final_name= "Sourav" + " "+ "kr"+" " +"jha"
print(final_name)
print(len(final_name))

print(final_name[2]) #indexing in python

print("here I'm trying slicing in the program",final_name[0:len(final_name)]) #slicing in python here {len(final_name) is the length full of the string}
print(final_name[:len(final_name)]) #slicing in python here {len(final_name) is the length full of the string}
print(final_name[0:])#This also indficates the full length of the string

#Backward Counting in negative order in slicing
str3="Apple"
print(str3[-4:-1]) #This will print {ppl}

#Starting the String functions
str5="Sourav"
print(str5.endswith("av")); #It prints True because it's checking last av is in the word or not if yes then it returns True. 

str6="sourav"
str6=str6.capitalize()
print(str6) #It will capitalize the first letter of the str6.

str7="My name is Sourav"
print(str7.replace("Sourav","Varun")) #It will replace the Sourav to varun here. 

str8="My subject is Python"
print(str8.find("subject")) #It will find the first word of on the entire sentence

str9="My name is Sourav kumar jha"
print(str9.count("a")) #It counts the word in the sentence. 

