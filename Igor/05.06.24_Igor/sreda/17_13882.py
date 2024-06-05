S = [int(x) for x in open("probnik/sreda/17_13882.txt")]
cnt=0
listansw=[]
maxKrat = max([x for x in S if x%401==0]) 
for i in range(len(S)-2):
    if S[i]+S[i+1] != S[i]+S[i+2] != S[i+2]+S[i+1]:
        if S[i]+S[i+1]+S[i+2]>maxKrat:
            cnt+=1
            listansw.append(S[i]+S[i+1]+S[i+2])
print(cnt,min(listansw))
