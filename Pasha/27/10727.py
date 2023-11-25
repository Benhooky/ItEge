f = [int(x) for x in open("ItEge/Pasha/27/27-A_10727.txt")]
cnt = 0
cntPos = 0
cntNeg = 0
f = f[1:]
for i in range(len(f) - 1):
    cntPos = 0
    cntNeg = 0
    if f[i] > 0:
        cntPos += 1
    elif f[i] < 0:
        cntNeg += 1
    if cntPos == cntNeg:
            cnt += 1
    for j in range(i + 1, len(f)):
        if f[j] > 0:
            cntPos += 1
        elif f[j] < 0:
            cntNeg += 1
        if cntPos == cntNeg:
            cnt += 1
    cntPos = 0
    cntNeg = 0
print(cnt)
