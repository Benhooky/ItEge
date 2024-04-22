f = open('ItEge/Artur/17/17_13088 (5).txt')
allNum = [int(x) for x in f]
max17 = -10000000000
cnt = 0
maxSum = -10000000000000
for i in allNum:
    if abs(i) % 100 == 17:
        max17 = max(max17, i)
for i in range(len(allNum)-2):
    troika = allNum[i:i+3]
    four = 0
    five = 0
    for chislo in troika:
        if 1000 <= abs(chislo) <= 9999:
            four += 1
        if abs(chislo) % 5 == 0:
            five += 1
    if four == 2:
        if five >= 1:
            if max17 < sum(troika):
                maxSum = max(maxSum , sum(troika))
                cnt += 1
print(cnt, maxSum)