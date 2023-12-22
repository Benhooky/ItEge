S = [int(i) for i in open("ItEge/Igor/17/1_17.txt")]
cnt = 0
max17 = 0
for i in S:
    if i%100==17:
        max17=max(max17,i)
for i in range(len(S) - 2):
    f =[S[i],S[i + 1],S[i + 2]]
    if sum(f)<max17:
        cnt3 = 0
        for j in f:
            if len(str(abs(j)))==3:
                cnt3+=1
        if cnt3==1:
            cnt+=1
print(cnt)
