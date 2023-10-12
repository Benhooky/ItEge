import math
S=[int(i) for i in open('17 (16.04).txt')]
Max=0
cnt=0
minS=2000000000000
for e in S:
    if ((int(math.log(e,10)+1))==3)and(e%10)==5:
        minS=min(minS,e)
for i in range(len(S)-1):
    if ((int(math.log(S[i],10)+1)==3)and(int(math.log(S[i+1],10)+1)!=3))or((int(math.log(S[i+1],10)+1)==3)and(int(math.log(S[i],10)+1)!=3)):
        if ((S[i]+S[i+1])%minS==0):
            cnt+=1
            Max=max(Max,((S[i]**2)+(S[i+1]**2)))
print(cnt,Max)