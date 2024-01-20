f = open('ItEge/Igor/9/9.txt')
cnt = 0
for s in f:
    flagPov = False
    flagUnique = False
    my_numbers = sorted(list(map(int, (s.split()))))
    if len(set(my_numbers)) == 2:
        for i in set(my_numbers):
            if my_numbers.count(i) == 3 and i%2 != 0:
                flagPov = True
            if my_numbers.count(i) == 1 and i%2 == 0:
                flagUnique = True
    if flagPov and flagUnique:
        cnt += 1
print(cnt)