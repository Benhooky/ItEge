f = open('ItEge/Artur/17/17_14952.txt')
allNumbers = [int(x) for x in f]
max121 = -100000000000
cnt = 0
maxSuma = -10000000000000000
for x in allNumbers:
    if abs(x) % 1000 == 121:
        max121 = max(max121, x)
for i in range(len(allNumbers)-2):
    tri = allNumbers[i:i+3]
    cntChet = 0
    for element in tri:
        if 1000 <= abs(element) <= 9999:
            if element % 2 == 0:
                cntChet += 1
    if cntChet <= 1:
        if sum(tri) <= max121:
            maxSuma = max(maxSuma, sum(tri))
            cnt += 1
print(cnt, maxSuma)
