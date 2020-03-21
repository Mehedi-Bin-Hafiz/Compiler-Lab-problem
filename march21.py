
file=open('march21.txt', 'r')
memo=[ ] #virtual memory
for i in file.read():
    if i!=" ":
        memo.append(i)
file.close()
up,low,alpha,dis,spe=0,0,0,0,0
for j in memo:
    if j.isupper()==True:
        up=up+1
        alpha=alpha+1
    elif j.islower()==True:
        low=low+1
        alpha = alpha + 1
    elif j.isdigit() == True:
        dis=dis+1
    else:
        spe=spe+1
print("Uppercase",up)
print("Lowercase",low)
print("Total alphabet",alpha)
print("Digit",dis)
print("Special character",spe)
