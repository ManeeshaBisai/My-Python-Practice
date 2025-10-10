# __init__Function
# Constructer
"""All classes have a function called __init__(),
   which is always executed when the class is being initiated."""

class student :

    #default constructors
    def __init__(self):
        pass

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")

s1 = student("Maneesha",99)
print(s1.name,s1.marks) # Maneesha

s2 = student("Sameera",97)
print(s2.name,s2.marks) #Sameera    