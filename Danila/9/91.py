f = open('ItEge/Danila/9/1214.txt')
cnt = 0
for i in f:
    sum_povt = 0
    my_numbers = sorted(int(x) for x in i.split())
    if my_numbers[0] != my_numbers[1]:
        if len(set(my_numbers)) != len(my_numbers):
            for j in set(my_numbers):
                if my_numbers.count(j) > 1:
                    sum_povt += j*my_numbers.count(j)
    if my_numbers[0]+my_numbers[-1] < sum_povt:
        cnt += 1
print(cnt)
