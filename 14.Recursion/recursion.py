"""Recursion = When a function calls itself repeeatedly."""
#prints n to 1 backwards

def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)
show(5)
show(7)
show(10)