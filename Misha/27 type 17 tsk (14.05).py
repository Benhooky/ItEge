S=[int(i) for i in open('27_A(17) (14.05).txt')]
Max=0
for i in range(len(S)-1):
    for j in range(i+1,len(S)):
        if (S[i]%160!=S[j]%160)and((S[i]%7==0)or(S[j]%7==0)):
            Max=max(Max,(S[i]+S[j]))
print(Max)