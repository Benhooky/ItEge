f = open("ItEge/Igor/komp/2098.txt")
cnt=0
for e in f:
    my_num = list(map(int,e.split()))
    if ((my_num[0]==0 and my_num[2]==0) or (my_num[0]==0 and my_num[3]==0) or (my_num[1]==0 and my_num[3]==0) or (my_num[1]==0 and my_num[2]==0)):
        cnt+=1
print(cnt)