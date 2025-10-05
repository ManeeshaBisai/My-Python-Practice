# Dictionary methods
student = {
    "name" : "Mani",
    "subjects" : {
        "maths" : 90,
        "phy" : 80,
        "comp" : 91
    }
}
print(list(student.keys())) #returns all keys # list
print(tuple(student.values())) #returns all values #tuple
print(student.items()) #returns all (key,value) pairs as tuples
print(student.get("subjects")) #returs the key according to value
new_dict = {"city" : "vizag","age":22}
student.update(new_dict) # adding the new_data into dictionary
print(student)