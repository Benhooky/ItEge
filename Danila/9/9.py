f = open('ItEge/Danila/9/41212.txt')
cnt = 0
for i in f:
    cnt += 1
    my_numbers = sorted(int(x) for x in i.split())
    if len(set(my_numbers)) == 5:
        sum_nepov = 0
        povt = 0
        for j in set(my_numbers):
            if my_numbers.count(j) > 1:
                povt = j
            else:
                sum_nepov += j
        if povt >= sum_nepov / 4:
            print(cnt)
            break
