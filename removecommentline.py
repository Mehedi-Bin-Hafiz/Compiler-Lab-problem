file=open('programewithcomments.txt', 'r')

memo=[ ] #virtual memory
for i in file:
   memo.append(i.rstrip('\n'))
file.close()
  # If its is not found then it returns -1 , if is found then return index number it may be  0 or more
for i in memo:

        if(i.find("'''")>-1 or  i.find("#")>-1):
            pass
        else:
            print(i)
            program=open('onlyprogram.txt','a')
            program.write(i+'\n')
            program.close()



