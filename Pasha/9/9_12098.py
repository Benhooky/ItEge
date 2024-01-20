f = open('ItEge/Pasha/9/12098.txt')
cnt = 0 
for i in f:
    s = [int(x) for x in i.split()]
    povt1 = False
    povt3 = False
    for j in set(s):
        if s.count(j) == 3 and j % 2 != 0:
            povt3 = True 
        elif s.count(j) == 1 and j % 2 == 0:
            povt1 = True
    if povt1 == True and povt3 == True:
        cnt += 1
print(cnt)
            