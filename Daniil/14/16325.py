value = 2*729**2014+2*243**2016-2*81**2018+2*27**2020-2*9*2022-2024
cnt = 0
while value > 0:
    if value%27 > 9:
        cnt+=1
    value = value//27
print(cnt)