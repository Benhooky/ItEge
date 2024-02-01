
minA = 10000000000
def checker(x,A):
    D = [x for x in range(7,69)]
    C = [x for x in range(29,101)]
    return ((x in D)<=(((not(x in C)) and (not(x in A))))<=(not(x in D)))
for Aleft in range(1,1000):
    for Aright in range(Aleft+1,1000):
        if Aright-Aleft > minA:
            break
        A = [x for x in range(Aleft,Aright+1)]
        if all(checker(x,A) for x in range(1,1000)):
            minA = min(minA,Aright-Aleft)    
print(minA)