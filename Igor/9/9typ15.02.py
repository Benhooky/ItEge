S = open("ItEge/Igor/9/9yandex.txt")
cnt=0
for i in S:
    my_numbers = (list(map(int, (i.split()))))
    cnt2 = 0
    for j in set(my_numbers):
        if my_numbers.count(j) == 2:
            cnt2+=1
    if cnt2 == 2 and my_numbers[0]== my_numbers[2]:
        cnt+=1
print(cnt) 
