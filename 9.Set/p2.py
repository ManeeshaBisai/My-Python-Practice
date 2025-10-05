"""Figure out a way to store 9,9.0 as separate values in the set.
   (you can take help of built-in data type)"""
#method 1
values = {"9",9.0}
print(values)
#method 2
values = {
    ("int",9),
    ("float",9.0)
}
print(values)