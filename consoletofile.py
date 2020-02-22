f1=None
f2=None
#fiel to console
try:
     f1=open("read.csv",'r')
except:
    print("file not found")
m=f1.read()
print( "Read form file: ", m)
f1.close()

#console to file
user=input("Enter strings:")
try:
     f2=open("write.csv",'w')
except:
    print("file not found")
f2.write(user)
f2.close()