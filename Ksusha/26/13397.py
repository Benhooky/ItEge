f=open('ItEge/Ksusha/26/26.7_13397.txt')
N=f.readline()
lst = [list(map(int,i.split())) for i in f]
lst = [[i[0],i[1]+i[0]] for i in lst]
#lst = [[int(i) for i in x.split()] for x in f]
lst=sorted(lst,key=lambda x: x[1])
cnt_p=1
timeFree = lst[0][1]
id = -1
bigDelay = 0
lstGood = []
for timeStart,timeFinish in lst[1:]:
    id+=1
    if timeFree<=timeStart:
        cnt_p+=1
        timeFree=timeFinish
        lstGood.append([timeStart,timeFinish])
lastTimeStart = sorted(lst,key=lambda x: x[0],reverse=True)[0][0]
print(cnt_p,lastTimeStart-lstGood[-2][1])