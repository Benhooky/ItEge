f = open("ItEge/Igor/9/11452.txt")
cnt = 0
for s in f:
    povt = 0
    cnt+=1
    sum_nepovt = 0
    my_numbers = sorted(list(map(int, (s.split()))))
    if len(set(my_numbers)) == 5:
        for i in set(my_numbers):
            if my_numbers.count(i) > 1:
                povt = i
            else:
                sum_nepovt += i
        if povt >= sum_nepovt / 4:
            print(cnt)
            break
