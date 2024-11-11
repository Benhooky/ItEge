res=216**1315-4*36**1502+5*36**1510-3*6**1331-253
cnt0 = 0
while res!=0:
    if res%6==0:
        cnt0 +=1
    res//=6
    print(cnt0)