# factorial of numbers

def fact(n):
    if(n == 0 or n == 1): # 0! = 1 , 1! = 1
        return 1
    else :
        return fact(n-1) * n # n! = (n-1)! * n
    
print(fact(3))
print(fact(5))
print(fact(7))