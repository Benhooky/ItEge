s=81**820-9**761-3**2022+14
cnt=0
while s!=0:
    if s%9==8:
        cnt+=1
    s=s//9
print(cnt)