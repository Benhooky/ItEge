file=open("Kate/27A(3)(04.06).txt")
N=int(file.readline()[:-1])
K=int(file.readline()[:-1])
S=[int(i) for i in file]
Min=20000000000000000000
for i in range(len(S)-300):
    for j in range(i+300,len(S)):
        if (S[i]*S[j])%157==0:
            Min=min(Min,(S[i]*S[j]))
print(Min)