v= input("Enter a String\n")
l=len(v)
print("length is : ",l)
if l > 10:
    v2=v
    print("first string is: ",v)
    print("first string is: ",v2)
else:
    v3= input("Enter another String\n")
    if(v3==v):
        print("first string is: ", v)
        print("first string is: ", v3)  #jgfsduihgiudfshg
    else:
        c1=len(v)
        c2=len(v3)
        m=max(c1,c2)
        if m==c1:
            print("first is bigger\n ", v+v3)
        elif m==c2:
            print("second is bigger"
                  "\n",v3+v)
        else:
            print('both are equal')