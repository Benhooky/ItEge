S = [int(x) for x in open("dz/17_13088.txt")]
cnt=0
listansw=[]
max17=max(x for x in S if str(x).endswith("17"))
for i in range(len(S)-2): 
    sumtroe=[S[i],S[i+1],S[i+2]]
    if ( (len(str(S[i]))==4 and len(str(S[i+1]))==4) or (len(str(S[i]))==4 and len(str(S[i+2]))==4) or (len(str(S[i+1]))==4 and len(str(S[i+2]))==4) ):
        if ( S[i]%5==0 or S[i+1]%5==0 or S[i+2]%5==0 ):
            if ( sum(sumtroe)>max17 ):
                cnt+=1
                listansw.append(sum(sumtroe))
print(cnt,max(listansw))