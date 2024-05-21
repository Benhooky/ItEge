r = 202**2024 + 223123**432
cnt = 0
while r>0:
    if r%27>9:
        cnt+=1
    r//=27
print(cnt)