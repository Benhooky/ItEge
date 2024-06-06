from collections import deque
d = deque([19,8,20,5,13,7])
n = 6
for i in range(n):
    sum1 = 0
    patrol = list(d)
    for j in range(1,len(patrol)//2):
        sum1+=patrol[j]*j+patrol[-j]*j
    if len(patrol)%2==0:
        sum1+=patrol[len(patrol[1:])//2+1]*len(patrol[1:])//2
    
    d.rotate(-1)
    
print(d)