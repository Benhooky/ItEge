f = open('ItEge/Artur/9/11658.txt')
number = 0
for string in f:
    number+=1
    string = sorted(int(x) for x in string.split())
    cnt3 = 0
    cnt1 = 0
    sred = 0
    for element in set(string):
        if string.count(element) == 3:
            cnt3 += 1
            sred = element
        if string.count(element) == 1:
            cnt1 += 1
    if cnt3 == 1 and cnt1 == 4:
        if sred > sum(string) / 7:
            print(number)