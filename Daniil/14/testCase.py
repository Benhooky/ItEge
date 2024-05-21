value = 45
cnt = 0
while value>0:
    if value%4>2:
        cnt+=1
    value = value // 4
print(cnt)