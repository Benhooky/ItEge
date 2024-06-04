f = open("dz/9_5946.txt")
cnt=0
for e in f:
    chet=0
    nechet=0
    my_num=sorted(list(map(int,e.split())))
    if len(set(my_num))==len(my_num):
        for num in my_num:
            if num%2==0:
                chet+=1
            else:
                nechet+=1
        if chet > nechet:
            cnt+=1
print(cnt)