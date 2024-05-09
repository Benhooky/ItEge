f=open('ItEge/Diana/27/27_B_7015.txt')
N=int(f.readline())
lst=[int(x) for x in f]
start = 0
end = 2
res=[]
while start!=N-1 and end!=N:
    if (lst[end-2]-lst[end-1])*(lst[end-1]-lst[end])<0:
        end+=1
    else:
        res.append(end-start)
        if lst[end]==lst[end-1]:
            start=end
            end+=2
        else:
            start=end-1
            end+=1
print(max(res))