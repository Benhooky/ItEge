f = open('ItEge/Artur/17/17_12735 (1).txt')
allNum = [int(x) for x in f]
max09 = -10000000000
cnt = 0
minMult = 10000000000000
for i in allNum:
    if abs(i) > 99:
        if abs(i) % 100 == 9:
            max09 = max(max09, i)
for i in range(len(allNum)-2):
    troika = allNum[i:i+3]
    semkrat = 0
    for chislo in troika:
        if abs(chislo) % 7 == 0:
            semkrat += 1
    if semkrat == 2:
        if max09 > sum(troika):
            cnt += 1
            minMult = min(minMult,troika[0]*troika[1]*troika[2])
print(cnt, minMult)