d = open("ItEge/Ksusha/17/17_11236.txt")
lis = [int(i) for i in d]
minkw = 100000000000
max4 = 0
cnt = 0
qqq = 0
for i in lis:
    if len(str(abs(i))) == 2:
        minkw = min(minkw, i**2)
    elif len(str(i)) == 4 and str(i)[-1] == "1":
        max4 = max(max4, i)
for i in range(len(lis) - 2):
    my_triple = sorted([lis[i], lis[i + 1], lis[i + 2]])
    min_value = my_triple[0]
    med_value = my_triple[1]
    max_value = my_triple[2]
    if med_value > minkw and min_value <= minkw:
        if abs(min_value * max_value * med_value) % max4 == 0:
            cnt += 1
            qqq = max(abs(min_value) + abs(max_value) + abs(med_value), qqq)
print(cnt, qqq)
