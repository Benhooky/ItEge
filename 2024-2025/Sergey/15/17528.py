minlen=10000000
for Aleft in range(100):
    for Aright in range (Aleft+1,100):
        flag=True
        for x in range (30,130):
            x/=2 
            if not ((15<=x<=40)<= (((21<=x<=63)and not(Aleft<=x<=Aright))<= (not(15<=x<=40)))):
                flag= False
                break
        if flag:
            minlen=min(minlen,Aright-Aleft)
print(minlen)