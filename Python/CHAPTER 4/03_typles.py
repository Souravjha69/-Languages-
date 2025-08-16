example01= (1,23,4,5,"String", True,5.14)
print("Printing the index [1] in the tuples list: ", example01[1])
print("Printing the trype of this data type example01: ", type(example01))

# Here I'm adding a new item in the tuple by creating new variable 
newexample01 = example01 + (69,) #We can't add item tuple directly so we have to create a new tuple with the new item.
print("Appended item here is in the tuple: ", newexample01)

