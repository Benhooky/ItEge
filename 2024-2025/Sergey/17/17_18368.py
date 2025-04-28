mas=[int(x) for x in open ("ItEge/2024-2025/Sergey/17/17_18368.txt")]
cnt=0
maxP=-100000000000000000000
min7=1000000000000000
for x in mas:
    if abs(x)%10==7:
        min7=min(min7,x)
for i in range(len(mas)-2):
    if 9999<abs(mas[i])<100000 or 9999<abs(mas[i+1])<100000 or 9999<abs(mas[i+2])<100000:
        if abs(mas[i]*mas[i+1]*mas[i+2])%min7==0:
            cnt+=1
            maxP=max(maxP,mas[i]*mas[i+1]*mas[i+2])
print(cnt,maxP)