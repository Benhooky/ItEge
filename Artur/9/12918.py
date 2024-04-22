f = open('ItEge/Artur/9/12918.txt')
for string in f:
    string = sorted([int(x) for x in string.split()])
    cntPovt2 = 0
    cntPovt1 = 0
    avgPovt = 0
    for element in set(string):
        if string.count(element) == 2:
            cntPovt2+=1
        elif string.count(element) == 1:
            cntPovt1+=1
    if cntPovt2 == 2 and cntPovt1 == 2:
        if string[-1] != string[-2]:
            if string[0]*string[-1]>sum(string[1:-1]):
                print(sum(string))
                break