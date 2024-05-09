n=49**7*7**20-7**8-28
cnt = 0
while n>0:
    if n%7 == 6:
        cnt+=1
    n//=7
print(cnt)