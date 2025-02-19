cnt = 0
for x in range(700001,10000000000000000):
    delit = []
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            delit.append(i)
            delit.append(x//i)
    delit = list(set(delit))
    delit.sort()
    M = max(delit)+min(delit) if len(delit)>1 else 0
    if M%10==4:
        print(x, M)
        cnt+=1
    if cnt==5:
        break