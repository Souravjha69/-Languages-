#So, in the Tuples are immutable , we cannot delete or add in Tuples here: -
list1=(1,2,3,45,6)
print("This is list1 :- ",list1)
print(list1[2]) #We can slice in the tuples here: - 
print(type(list1))

#Example
list2=(0,) #so here , comma is important because it shows the that it is tuple otherwise it shows integer here
print(type(list2))

#Count
list3=(1,2,3,4,6,4,3,3)
print("Count of Tuple", list3.count(3)) #Count the elements of 3.