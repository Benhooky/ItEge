f=open("ItEge/Ksusha/27/27-A_11957.txt")
first=[int(x) for x in f.readline().split()]
n = first[0]
t = first[1]
k = first[2]
lst = [list(map(int,x.split())) for x in f]
max_v=0
for i in range(n-t):
    for j in range(i+t,n):
        cnt_a=k//(lst[i][0])
        result=cnt_a*(lst[j][1])+k%(lst[i][0])
        max_v = max(max_v,result - k)
print(max_v)