f = open('ItEge/Stepan/9/12726.txt')
number = 0
lst = []
for line in f:
    number+=1
    line = sorted([int(x) for x in line.split()])
    cnt3 = 0
    cnt1 = 0
    for x in set(line):
        if line.count(x)==3:
            cnt3 += 1
        if line.count(x)==1:
            cnt1 += 1
    first = (cnt3 == 1 and cnt1 == 4)
    second = len([x for x in line if x % 2 == 0]) > len([x for x in line if x % 2 != 0])
    if first and second:
        lst.append(number)
print(max(lst))