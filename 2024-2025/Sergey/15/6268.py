minLen=1111111111111111
for Aleft in range(20,81):
    for Aright in range(Aleft+1,100):
        flag=True 
        for x in range(0,200):
            x=x/2
            if not(((not(23<=x<=37))<=(41<=x<=73))<=(Aleft<=x<=Aright)):
                flag=False
                break
        if flag:
            minLen=min(minLen,Aright-Aleft)
print(minLen)