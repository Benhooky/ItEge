f = [int(x) for x in open("probnik/17_1997.txt")]
cnt=0
m1=-20000
listansw=[]
for e in range(len(f)-1):
    if (((f[e]%2==0 and f[e]%4==0) and (f[e+1]%2!=0 and f[e+1]%11==0)) or ((f[e]%2!=0 and f[e]%11==0) and (f[e+1]%2==0 and f[e+1]%4==0))):
        listansw.append(f[e]+f[e+1])
        cnt+=1
print(cnt,max(listansw))

