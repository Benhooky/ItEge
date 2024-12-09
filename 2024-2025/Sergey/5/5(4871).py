s=0
for N in range(2,100000):
    if N%3==0:
        N=N//3
    else: 
        N=N-1
    if N%5==0:
        N=N//5
    else:
        N=N-1
    if N%11==0:
        N=N//11
    else:
        N=N-1
    R=N
    if R==8:
        s+=1
print(s)

