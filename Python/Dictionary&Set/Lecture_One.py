info ={
    "name": "Sourav kumar jha",
    "Company Name": "CyberSigma Consulting Services",
    "Position":"Software Developer",
    "Subjects":["Java", "Python","Cpp" ],
    "Numbers":(24,55,44,55),
    34:25.5
}
print("Printing the value of Key and Value Pairs: ", info)

#Now this is the example of key value pairs also "name" is the key "Sourav kumar jha" is a pair. 
# Dictionary is mutable.
# We can create duplicate keys. 

#If we have to access the value of the dictionary here: -
print(info["name"])

#If we have to add new key in dictionary : -
info["Dream"]="Japan"
print(info)