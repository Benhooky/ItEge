f = open('ItEge/Igor/26/26_15341.txt')
N = int(f.readline())
korzh = sorted([int(x) for x in f], reverse=True)
currentK = korzh[0]
cnt = 1
for element in korzh[1:]:
    if currentK-element>=8:
        cnt+=1
        currentK = element
print(cnt,currentK)