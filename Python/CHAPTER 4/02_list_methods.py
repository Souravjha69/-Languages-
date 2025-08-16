Example = ["Sourav", 69, "Python", 3.14, True]
print("Example list:", Example) #Whole index printing

# Append method example means i can add a new item in the list.
Example.append(False) # Addeing a new item in the list here "That is called append function"
print("And here the item [False] is added is added ",Example)


# Here I'm going to try the example of Sorting method
L1 = [2,45,98,892, 1, -98 ]
L2 = L1.sort()
print("So here is the example of sorting method:,",L1) # Ascending order is here follows.

Desc = [99,199,1,781,2,3,4,87]
Desc.sort(reverse=True)
print("Descending order is here follows:",Desc) # Descending order is here follows.


L3 = [24,58,7893,98, 1, -98 ]
Reverse = L3.reverse()
print("Here this is the reversed form of list: ", L3) #It's just reversed the list.

# Here I'm showing the example of Inserting at fixed index
insert = [1,67,98,56,98,-0]
insert.insert(2, 69) # Here 2 is the index and 69 is inserting at 2nd index means 
print("Inserted 69 index in the list: ", insert)

#Here I'm deleting element ata particular index
delete = [1,67,98,56,98,-0]
delete.pop(2) # Here 2 is the index and it will delete the element at 2nd index
print("Deleted element at index 2: ", delete) # Deleted the element at index 2
print(delete.pop(2)) #Here it will print the deleted element at index 2

#Here I'm showing the example of removing an element from the list
remove = [1,67,98,56,98,-0]
remove.remove(remove[4]) # Here it will remove specific element in the list and operating as their index
print("Removed element 98 from the list:", remove)