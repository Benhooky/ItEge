file=open("Kate/28129_A.txt")
N=int(file.readline()[:-1])
S=[int(i) for i in file]
Max=0
first=0
second=0
for i in range(len(S)-1):
    for j in range(i+1,len(S)):
        if (S[i]%160!=S[j]%160)and((S[i]%7==0)or(S[j]%7==0)):
            if Max<S[i]+S[j]:
                first=S[i]
                second=S[j]   
                Max=S[i]+S[j]     
print(first,second)