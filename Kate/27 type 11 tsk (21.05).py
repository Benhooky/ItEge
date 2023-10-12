file=open('27_A(11) (21.05).txt')
nNumber=file.readline()[:-1]
S=[int(i) for i in file]
Max=0
for i in range(len(S)-1):
    for j in range(i+1,len(S)):
        if (S[i]>S[j]):
            if (Max<(S[i]+S[j]))and((S[i]+S[j])%120==0):
                a=S[i]
                b=S[j]
                Max=max(Max,(S[i]+S[j]))
print(a,b)