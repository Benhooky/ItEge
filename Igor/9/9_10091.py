f = open('ItEge/Igor/9/92424.txt')
cnt = 0
for s in f:
    sum_povt = 0
    my_numbers = sorted(list(map(int, (s.split()))))
    if my_numbers[0] != my_numbers[1]:
        if len(set(my_numbers)) != len(my_numbers):
            for i in set(my_numbers):
                if my_numbers.count(i) > 1:
                    sum_povt += i*my_numbers.count(i)
    if my_numbers[0]+my_numbers[-1] < sum_povt:
        cnt += 1
print(cnt)
