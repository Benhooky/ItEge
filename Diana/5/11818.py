def F(x):
    s=""
    arr="0123456789AB"
    while x>0:
        s= str(arr[x%12])+ s
        x//=12
    return s

res=[]
for i in range(1,10000):
    if i%4==0:
        r=int("2"+F(i)+"64",12)
    else:
        r=int(F(i)+max(F(i)),12)
    if r>1799:
        res.append(r)
print(min(res))
