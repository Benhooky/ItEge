value = 3*3125**9+2*625**8-4*625**7+3*125**6-2*25**5-2024
cnt = 0
while value > 0:
    if value%25 == 0:
        cnt+=1
    value = value//25
print(cnt)
