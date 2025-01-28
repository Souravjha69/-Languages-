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