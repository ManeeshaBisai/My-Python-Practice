#WAF to give input num even or odd

def found(num):
    if num % 2 == 0:
        print("its an even number")
    else:
        print("its an odd number")

number = int(input("enter a num:"))
found(number)