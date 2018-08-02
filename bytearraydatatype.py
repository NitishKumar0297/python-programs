elements=[3,7,45,8,9]
x=bytearray(elements) #we can modified it
for i in x:print(i)
x[0]=0
x[1]=6
x[2]=7
print("modified array ")
for i in x:print(i)
