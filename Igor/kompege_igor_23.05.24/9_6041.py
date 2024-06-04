f = open("dz/9_6041.txt")
cnt=0
for e in f:
    my_num=sorted(list(map(int,e.split())))
    if len(set(my_num))==len(my_num):
        if my_num[2]<my_num[0]+my_num[1]:
            cnt+=1
print(cnt)