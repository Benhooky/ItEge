f=open('ItEge/Diana/27/27-B_937.txt')
N=int(f.readline())
lst=[sorted([int(y) for y in x.split()]) for x in f]
arr=[]
s1=0
s2=0
s3=0
minRaz = 1000000000
for i in range(N):
    s1+=lst[i][0]
    s2+=lst[i][1]
    s3+=lst[i][2]
    if (lst[i][2]-lst[i][1])%2!=0:
        minRaz = min(minRaz,lst[i][2]-lst[i][1])
    if (lst[i][2]-lst[i][0])%2!=0:
        minRaz = min(minRaz,lst[i][2]-lst[i][0])
print(s3-minRaz)