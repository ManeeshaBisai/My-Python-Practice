"""Range = Range functions returns a sequence of numbers,
   starting from 0 by default,and increments by 1(by default),
   and stops before a specified number."""

for el in range (5): # range(Start)
    print(el)

for el in range(1,5): # range(start,Stop)
    print(el)

for el in range(1,5,2): # range(start,stop,Step)
    print(el)