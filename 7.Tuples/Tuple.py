"""Tuple = A tuple is collection of items in python that is ordered and unchangeable.
   Think of a tuple like a box that's sealed - you can look at the items,
   but you can't change them after creating it."""

Tup = (2,1,3,1,1)
print(Tup[0]) #idx value of tuple
print(type(Tup)) #type of tuple
print(len(Tup)) #length of tuple
print(Tup[1:3]) #slicing of tuple

# Methods
print(Tup.index(2))
print(Tup.count(1))