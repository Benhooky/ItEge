from math import ceil
for a in range(1,1000):
    if ceil(a*9/8)*575>100*1024:
        print(a)
        break