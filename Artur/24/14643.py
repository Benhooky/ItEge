f = open('ItEge/Artur/24/24.13_14643.txt').readline()
keeperS = ''
maxlen = 0
for letter in f:
    keeperS += letter
    if 'AXMM' in keeperS:
        maxlen = max(maxlen, len(keeperS) - 1)
        keeperS = keeperS[-3:]
print(maxlen)