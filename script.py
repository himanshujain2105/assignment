a=input("enter a text to add to the file:")
f2=open('output.txt','w')
w2=f2.write(a)
f2.close()
print("data sucessfully written in the file")
b=input("enter additional text to append:")
with open('output.txt','a')as f2:
      a=f2.write(b)
print("data sucessfully appended")
with open('output.txt','r')as f2:
    r1=f2.read()
    print("final content of this file")
    print(r1)
