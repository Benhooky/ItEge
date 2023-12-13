f=open('ItEge/Ksusha/9/first.txt')
cnt = 0
for my_str in f:
    is_valid = True
    sum_povt = 0
    sum_uniq = 0
    cnt_povt=0
    my_str=sorted([int(i) for i in my_str.split()])
    for i in set(my_str):
        if my_str.count(i)==2:
            cnt_povt+=1
            sum_povt+=i
        elif my_str.count(i)==1:
            sum_uniq+=i
        else:
            is_valid = False
    if cnt_povt==2 and sum_povt>sum_uniq and is_valid:
        cnt+=1
print(cnt)



