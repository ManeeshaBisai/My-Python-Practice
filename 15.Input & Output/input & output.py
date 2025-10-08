f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
#line1 = f.readline() #read line
#print(line1) #read line
f.close()