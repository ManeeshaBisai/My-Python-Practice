"""WAP to enter marks of 3 subjects from the user and store them in a dictionary.
   start with an empty dictionary & add one by one.
   use subject name as key & marks as value."""

marks = {}

x = int(input("enter phy marks :"))
marks.update({"phy" : x})

y = int(input("enter maths marks :"))
marks.update({"maths" : y})

z = int(input("enter comp marks :"))
marks.update({"comp" : z})

print(marks)