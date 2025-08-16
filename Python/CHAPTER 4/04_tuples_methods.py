# example01 = (12,13,14,15,"String", False, 3.14,13,13)
# print("Count here", example01.count(13))
# newexample01 = example01.count(13)
# print("newexample01: ", newexample01) # It's printing the count of 13 in the tuple means how many times 13 came in the tuple.

# Returning the index Number:
example02 = (1,2,3,4,5,6,7,8,9)
newexample02 = example02.index(4)
print("Index of 4 in example02 tuple is : ", newexample02) # Here we are finding the index of 4 in the tuple example02 and it will return the index number of that element.

#Returning the count like how many time this comes in the tuple:
example01 = (1, 23, 4, 5, "String", True, 5.14)
newexample01 = example01.count(5)
print("Returing the element in the index 5 in the tuple: ", newexample01) # It's printing the count of 5 in the tuple means how many times 13 came in the tuple.

#Concatenating tuples:
example03 = (1,2,3)
example04 = (4,5,6)
newexample34 = example03 + example04
print("Concatenated tuple example03 and example04: ", newexample34) # Here we are concatenating two tuples example03 and example04, it means we are joining them together to make a new tuple.

# Repeating tuples:
example05 = (1,2,34,5,6,7,7,78)
newexample05 = example05 * 4
print("Here we are repeating the tuple 4 times in single tuple: ", newexample05)