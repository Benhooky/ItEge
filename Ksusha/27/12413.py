s=open('ItEge/Ksusha/27/27A_12413.txt')
n=int(s.readline())
lis=[int(x) for x in s]
cnt=0
s='4123412411124'
s.count('1')
for i in range (0,len(lis)-3):
    for j in range (i+1,len(lis)-2):
        for k in range (j+1,len(lis)-1):
            for h in range (k+1,len(lis)):
                qr =sorted([lis[i], lis[j], lis[k], lis[h]])
                if qr[0]==qr[1] and qr[2]==qr[3]:
                    cnt+=1
print(cnt)