
for x in range(67):
    s1 = f'3{x}21'[::-1]
    s2 = f'17B{x}4'[::-1]
    sum1 = 0
    sum2 = 0
    for i in range(len(s1)):
        sum1 += int(s1[i],36)*81**i
    for i in range(len(s2)):
        sum2 += int(s2[i],36)*67**i
