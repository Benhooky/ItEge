S = [int(x) for x in open("ItEge/Igor/17/17_11703.txt")]
max18 = -20000
cnt=0
maxx = -100000000
for i in S:
    if str(i)[-2:]=="18":
        max18=max(i,max18)
for i in range(len(S)-2):
    numbers = [abs(S[i]),abs(S[i+1]),abs(S[i+2])]
    numbers = [len(str(x)) for x in numbers]
    if (any(x==5 for x in numbers) and (S[i]*S[i+1]*S[i+2])%max18==0):
        cnt += 1
        maxx = max(maxx, S[i] * S[i+1]*S[i+2])
print(cnt,maxx)