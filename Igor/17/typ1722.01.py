S = [int(x) for x in open("ItEge/Igor/17/17 (3).txt")]
maxx = -20000
cnt=0
for i in range(len(S)-1):
    if (abs(S[i])%3==0 or abs(S[i+1])%3==0):
        cnt += 1
        maxx = max(maxx, S[i] + S[i+1])
print(cnt,maxx)