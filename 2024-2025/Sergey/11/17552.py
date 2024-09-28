from math import ceil 
for i in range (0,100000):
    if ceil(261*i/8)*252500>31*2**20:
        print(i)
        break