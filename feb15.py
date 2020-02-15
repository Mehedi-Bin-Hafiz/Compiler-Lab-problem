f1=None
f2=None
try:
     f1=open("read.csv",'r')
except:
    print("file not found")
m=f1.read()
print( "Read form file: ", m)
f1.close()
try:
     f2=open("write.csv",'w')
except:
    print("file not found")
f2.write(m)