#WAP to print Grade of students based on marks.
marks = int(input("enter your marks:"))
if marks >= 90:
    print("A")
elif 90 > marks >= 70:
    print("B")
elif 70 > marks >= 50:
    print("C")
elif 50 > marks >= 35:
    print("D")
else:
    print("fail")