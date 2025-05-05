from math import ceil

for i in range(1,10000):
    if ceil(119*i/8)*125300>=23*2**10*2**10:
        print(i)
        print(2**(i-1)+1)
        break