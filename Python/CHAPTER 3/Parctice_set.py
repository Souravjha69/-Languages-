#Q1.
Program = (input("Enter the User name:"))
print ("Good Afternoon ",(Program),"!")
print (f"Good Afternoon {Program}") #This is f string we can do by this way also 

#Q2.
ProgramName = (input("Enter the name:"))
ProgramDate = (input("Enter the date:"))
print("Dear",(ProgramName),",\nYou are selected!","\n",(ProgramDate))
letter = '''Dear <|Name|>,
            You are selected!
            <|Date|>'''
print (letter.replace("<|Name|>","Sourav kumar jha").replace("<|Date|>", "24th July, 2025"))

#Q3. 
Name = "Sourav kumar jha is really a  good boy"
print ("Finding the double space here:", Name.find("  "))

#Q4.
Name = "Sourav kumar jha is really a  good boy"
print ("Replacing the double space here:", Name.replace("  "," "))

#Q5.
print ("\"Dear Harry, this Python course is nice. Thanks!\"")

#Note: - String are immutable means we cannot change them by running functions original strings. 