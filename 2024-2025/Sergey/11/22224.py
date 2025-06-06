from math import ceil
for i in range(1,100000000):
    if ceil(i*94/8)*205000>7*1024*1024:
        print(i)
        break