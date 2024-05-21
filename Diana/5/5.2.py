def tri(x):
    s=''
    while x:
        s=str(x%3)+s
        x=x//3
    return(s)
res=[]
for n in range(11,1000):
    s=tri(n)
    if s.count('1')<(len(s)-s.count('1')):
        s='22'+s
    else: s='11'+s
    r=int(s,3)
    if r>100:
        res.append(r)
print(min(res))