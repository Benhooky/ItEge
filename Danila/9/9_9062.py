f = open("ItEge/Danila/9/9_9062.txt")
cnt = 0
for i in f:
    mylist = list(map(int, i.split()))
    if (
        mylist[0] != max(mylist)
        and mylist[0] != min(mylist)
        and mylist[-1] != max(mylist)
        and mylist[-1] != min(mylist)
    ):
        mylist.sort()
        if mylist[2] != mylist[1]:
            if (mylist[-1] - mylist[0]) % (mylist[2] - mylist[1]) == 0:
                cnt += 1
print(cnt)
