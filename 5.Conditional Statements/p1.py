#WAP to check the signal light color and print what to do.
light_color = str(input("enter a color:"))
if(light_color == "red"):
    print("Stop")
elif(light_color == "green"):
    print("Go")
elif(light_color == "yellow"):
    print("Get ready")
else:
    print("Invalid color")