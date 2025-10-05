"""if-elif-else Statement = if-elif-else statement is used to make decisions in python.
   if chacks different conditions,and runs the code based on which condition is true."""
age = int(input("Enter your age:"))
if(age > 18):
    print("Adult")
elif(age == 18):
    print("just became adult")
else:
    print("Not adult")