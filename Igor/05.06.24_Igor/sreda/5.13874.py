listansw=[]
def chech(x):
    y=''
    while x>0:
        y+=str(x%4)
        x//=4
    return y[::-1]
for n in range(1,1000):
    i=chech(n)
    if n%3==0:
        i = i[-1] + i[1:-1] + i[0] + "1"
    else:
        i=i+str(int(i)%3)
    r=int(i,4)
    if r<=340:
        listansw.append(r)
print(max(listansw))