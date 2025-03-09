cntA=0
for A in range (1,10000):
    flag=True 
    for x in range (1,10000):
        if not((x%A==0) or ((170<=x<=220)<= (not(x%24==0)))):
            flag=False 
            break 
    if flag:
        cntA+=1
print(cntA)