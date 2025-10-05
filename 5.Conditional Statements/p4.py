#WAP to find the greatest of 3 numbers entered by the user.
num1 = int(input("enter 1st number:"))
num2 = int(input("enter 2nd number:"))
num3 = int(input("enter 3rd number:"))
if num1 > num2 and num3:
    print("num1 is greatest of all.")
elif num2 > num3 and num1 :
    print("num2 is greatest of all.")
else :
    print("num3 is greatest of all.")