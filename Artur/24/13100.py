f = open('ItEge/Artur/24/24_13100 (3).txt').readline()
keeperS = ''
maxlen = 0
for letter in f:
    keeperS += letter
    if keeperS.count('C') == 3 or keeperS.count('D') == 3:
        maxlen = max(maxlen, len(keeperS) - 1)
        keeperS = keeperS[keeperS.index(keeperS[-1])+1:]
print(maxlen)