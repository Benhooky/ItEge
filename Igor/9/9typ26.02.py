def unik(x):
    x=[]
    unique_elements = []

    for item in x:
        if item not in unique_elements:
            unique_elements.append(item)


f = open("ItEge/Igor/9/926.txt")
cnt=0
number = 0
for e in f:
    number+=1
    my_num=sorted(list(map(int,e.split())))
    cnt3 = 0
    cnt1 = 0
    avgPovt = 0
    for i in set(my_num):
        if my_num.count(i) == 3:
            cnt3 +=1
            avgPovt = i 
        elif my_num.count(i) == 1:
            cnt1 +=1
    if cnt3 == 1 and cnt1 == 4:
        if sum(my_num)/len(my_num) < avgPovt:
            print(number)