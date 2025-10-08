f = open("demo.txt","r")
#data = f.read() #reads entire file
#data = f.readline() #reads one line at a time
#print(data)
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
f.close()