info ={
    "name": "Sourav kumar jha",
    "Company Name": "CyberSigma Consulting Services",
    "Position":"Software Developer",
    "Subjects":["Java", "Python","Cpp" ],
    "Numbers":(24,55,44,55),
    34:25.5
}
print(info.keys()) #In this we are accessing only keys.
print(info.values()) #In this we are accessing only values.
# print("As a Tuples: ",info.items()) It returns all the values as tuples.
print(info.get("keys"))

newInfo={
    "name": "Sourav kumar jha",
    "Company Name": "CyberSigma Consulting Services",
    "Position":"Software Developer",
    "Subjects":["Java", "Python","Cpp" ],
    "Numbers":(24,55,44,55),
    34:25.5
}

print(newInfo) 
print(len(newInfo))
print(len(newInfo["Numbers"]))
print(list(newInfo.values()))
pairs= list(newInfo.items)
print(newInfo[0])