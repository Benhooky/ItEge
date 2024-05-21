value = 4*3125**2019+3*625**2020 - 2 * 125 ** 2021 + 25 ** 2022 - 4 * 5 ** 2023 - 2024
cnt = 0
while value>0:
    if value%25>10:
        cnt+=1
    value = value // 25
print(cnt)