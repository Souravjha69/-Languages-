#Indexing of the string
str="Sourav kumar jha"
ch=str[2]
print(ch)
print(str[5])

#Slicing of the String
sli=str[0:6]
print(sli) #Here Starting index included but Ending index don't. 
print(str[:6]) #[0:6] Starting from 0 automatically
print(str[0:]) #[0:len[str]] starting from 0 but ended end of string

#Negative slicing of the index
str2="Swati"
print(str2[-3:-1])

#String Function's
str3="I am learning Python from Apna College"
print(str3.endswith("ege")) #It shows string's ends with ege or not if not then output will be false

#Replace the string
str4="I am learning Python"
str4=str4.replace("Python","Javascript") #It replaces the original string
print(str4.replace("Python","Javascript"))
print(str4)

#Finding the string
print(str4.find("g")) #It returns the index of that string

#Count the string
print(str4.count("n"))