# Simple functions of Strings: -

FullName = "Souravkumarjha"
ShortName= FullName[0:6]
NegativeShortName= FullName[-14:-8]
# 1. Slicing
print("Here I'm printing my short name by slicing: ",ShortName)
print("Here I'm printing my short name by negative slicing: ",NegativeShortName)
print("Here I'm just printing the slicing and testing different types of slicing:", FullName[:5],"Second Test: ", FullName[1:], "Third Test: ", FullName[3:6])
# 2. Length of String
print("Length of my full name is: ",len(FullName))
