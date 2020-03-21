
file=open('ExtraNewLineAndSpace.txt', 'r')

memo=[ ] #virtual memory
for i in file:
   memo.append(i.rstrip('\n'))

file.close()

for i in memo:
        if(i==''):
            pass
        else:

            program=open('ProgramWithExtraSpace.txt','a')
            program.write(i+'\n')
            program.close()


#### this file act as a media###
file2=open('ProgramWithExtraSpace.txt', 'r')
memo2=[ ] #Extra new line removed but extra space exist;
for i in file2.read():
   memo2.append(i.rstrip('\n'))
file.close()
file2=open('ProgramWithExtraSpace.txt', 'w')
file2.write("")
file2.close()

#print("memo2",memo2)
#### this file act as a media###

memo3=[]
bp=None
fp=0
count=0
for bp in memo2:
    if(bp==' '):
        fp=count-1
        if(fp<0):
            fp=0
        if(memo2[fp]==' '):
            pass
        else:
            memo3.append(bp)  # it store NoExtraSpace but include at least 1 space;
    else:
        memo3.append(bp) # it store string.
    count=count+1


final=open('CodeWithNoExtraSpace.txt','a')
for element in memo3:
    if(element==''):
        final.write('\n')
    else:
        final.write(element)


