#Q1. Length Check
# Take a user's full name as input and print the total number of characters (including spaces).
# name = input ("Enter your full name: -")
# print("Total number of the characters are: -" , len(name))

# Q2. Case Conversion: -
# Convert a given string into all:
# lowercase
# uppercase
# title case

# Name = input ("Enter your City Name: ")
# print("Lowercase of the character: ", Name.lower())
# print("Uppercase of the character: ", Name.upper())
# print("Tittle case of the character: ", Name.title())

# Q3. Remove Whitespace
# Ask the user to input a string with extra spaces at the start and end. Remove those spaces and print the cleaned version.

UserName = input("Enter your User Name: ")
print("Removing the extraspace in the string:", UserName.strip())   

# Q4. Replace Words
# Replace all occurrences of the word "bad" with "good" in the sentence:
# "Python is not bad, it's really bad!"

Sentence = "Python is not bad, it's really bad!"
print("Sentence replacing bad with good: ", Sentence.replace("bad", "good"))

# Q5. Count Occurrences
# Count how many times the letter 'a' appears in the user's input string.

Counting = "souravkumarjha"
print("Here I'm printing the count occurences: ", Counting.count("a"))

# Q6. Find Index
# Ask the user to enter a sentence and find the position of the first space character.

Sentence =  input("Enter a sentence: ")
print("The position of the first space character is: ", Sentence.find("g"))

# Q7. Check Start and End
# Ask the user for a file name and check:
# Does it start with "data_"?
# Does it end with ".csv"?

Data = input("Enter your File Name: ")
print("Is your file name starts with", Data.startswith("data"))
print("Is your file name ends with", Data.endswith(".csv"))

# Q8. Split and Join
# Input a sentence and split it into words.
# Then join the words using a hyphen (-) instead of spaces.

Sentence = input("Enter your sentence: ")
print("Splitting the sentence", Sentence.split())
print("Joining the sentence: ", "-".join(Sentence.split()))

# Q9. Check Content
# Ask the user to enter a password:
# Check if it’s only digits using .isdigit()
# Check if it’s only letters using .isalpha()
# Check if it’s alphanumeric using .isalnum()

Password = input("Enter a password: ")
print("is your password only digits: ", Password.isdigit())
print("is your password only letters: ", Password.isalpha())
print("is your password alphanumeric: ", Password.isalnum())    

# Q10. Capitalize Sentence
# Convert the first character of the sentence to uppercase, and the rest to lowercase.

Sentencehere = input("Enter the new sentence")
print("Capitalize the sentence: ", Sentencehere.capitalize())