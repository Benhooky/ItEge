f = open("ItEge/Pasha/9/9probnik.txt")
lis = [list(map(int, x.split())) for x in f]
listOfColums = [[x[i] for x in lis] for i in range(5)]
lisOfDict = [dict1 := {}, dict2 := {}, dict3 := {}, dict4 := {}, dict5 := {}]
for dictIndex, currentDict in enumerate(lisOfDict):#5 проходов
    for i in listOfColums[dictIndex]:#16000 проходов
        if i not in currentDict.keys():
            currentDict[i] = listOfColums[dictIndex].count(i)
answer = 0
for number,j in enumerate(lis,1):
    cntOk = 0
    cntSame = 0
    for l in range(len(j)):
        if any(x % 2 == 0 for x in j[l + 1:]):
            cntOk += 1
        if j.count(j[l]) == lisOfDict[l][j[l]]:
            cntSame +=1
    if cntOk >= 3 and cntSame >= 1:
        answer = number
print(answer)