f = open("ItEge/Danila/9/9_8667.txt")
cnt = 0
for i in f:
    mylist = sorted(list(map(int, i.split())))
    if len(mylist) == len(set(mylist)):
        if ((mylist[0] + mylist[-1]) * 5) >= ((sum(mylist[1:-1])) * 3):
            cnt += 1
print(cnt)
