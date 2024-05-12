S = [int(x) for x in open("dz/17_2311.txt")]
cnt=0
listansw=[]
maxnechet = max(x for x in S if x%2!=0) 
for i in range(len(S)-1):
    if ( (S[i]+S[i+1])*2 > maxnechet ):
        cnt+=1
        sumS=S[i]+S[i+1]
        listansw.append(sumS)
print(cnt,min(listansw))
        