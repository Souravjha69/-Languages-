# Here in this list we will change the list items but in the strips we cant change the string itmes means index items in the middle.
# So, I can say lists are mutable and strings are immutable.

Example = ["Sourav", 69, "Python", 3.14, True]
Example[1] = 89 #Changing the 2nd item in the list
print("Example list:", Example) #Whole index printing
print("Printing the 3rd item in the list:", Example[3]) #Printing the 3rd item in the list
print("Printing the changed 2nd item in the list:", Example[1]) #Printing the changed 2nd item in the list

# Exmple of Indexing slicing here: -
Example2 = ["Sourav", 69, "Python", 3.14, False, "Java", "Apple"]
print("Here we slicing the list (Indexing):", Example2[1:4]) # As we know the last item in the list is not included in the slicing.
