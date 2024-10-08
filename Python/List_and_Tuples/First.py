marks=[22,55,34.5,33.6,99.8,66.5]
print(type(marks))
print(marks[1]) #Printing the index
marks[0]="Sourav" #We can replace the value in list 
print(marks)
print(marks[0:3])#Slicing is also Possible in List
list2=[4,3,45,5]
list2.append(4) #Mutation add the element in list
print(list2)
new=list2.sort() #Sort in ascending order 
print(list2) 

list3=[24,45,67,87]
print(list3.sort(reverse=True))
print(list3)

#Reverse the list
list4=[12,33,44,55]
list4.reverse()
print("This is list4: - ",list4)

#Adding elements with index in list
list5=[23,44,55,66]
list5.insert(1,123)
print("This is list 5:- ",list5)

#Remove the element directly from the list
list6=[434,55,677,77]
list6.remove(434)
print("This is list 6:- ",list6)

#Remove the element particularly from the index
list7=[33,55,66,77,878]
list7.pop(1)
print("This is list7:- ", list7)