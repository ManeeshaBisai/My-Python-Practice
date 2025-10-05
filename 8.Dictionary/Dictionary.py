"""Dictionary = Dictionaries are used to store data values in key:value pairs
   They are unordered,mutable & don't allow duplicate keys."""

info = {
    "name" : "Maneesha",
    "age" : 22 ,
    "CGPA" : 80.00 ,
    "is_adult" : True,
    "subjects" : ["python","c","java"] ,
    "topics" : ("Dict","sets")
}
info["surname"] = "Bisai" #overwrite
print(info)
print(type(info)) #type of dict
print(len(info)) #length of dict
print(info["name"]) #print only dict value