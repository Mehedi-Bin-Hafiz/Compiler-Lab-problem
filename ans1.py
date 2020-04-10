string="my name is Mehedi. some symbols are ( ) { } ;  : and some digits are 1 2 3 4 5"
memo=[]

for i in string:
    if i!=" ":
        memo.append(i)
print(memo)
digit=[]
sym=[]
up,low,alpha,dis,spe=0,0,0,0,0
for j in memo:
    if (j >= '0' and j <= '9'):
        digit.append(j)
    elif ((j >= 'a' and j <= 'z') or (j >= 'A' and j <= 'Z')):
        pass
    else:
        sym.append(j)

print(digit)
print(sym)