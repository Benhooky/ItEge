mas = [(1,2),(11,2),(1,12),(11,12),(-11,-12),(-11,12),(-12,11),(10,10),(10,5)]
cntA = 0
for A in range (-100,100):
    cntYes = 0
    for s,t in mas:
        if (s>10) or (t>A):
            cntYes += 1
    if cntYes == 7:
        cntA += 1
print(cntA)