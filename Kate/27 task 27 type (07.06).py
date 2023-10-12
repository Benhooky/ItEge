file=open("Kate/28133_B.txt")
N=int(file.readline()[:-1])
S=[int(i) for i in file]
Max=0
a=0
b=0
for i in range(len(S)-1):
    for j in range(i+1,len(S)):
        if (S[i]>S[j])and(i<j<=N):
            if (S[i]+S[j])%120==0:
                if (S[i]+S[j])>=Max:
                    Max=(S[i]+S[j])
                    a=S[i]
                    b=S[j]
print(a,b)