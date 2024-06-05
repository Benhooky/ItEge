from fnmatch import *
for i in range(2024,10**10,2024):
    if fnmatch(str(i),"112?57*4"):
        if sum(map(int,str(i)))%2!=0:
            print(i,i//2024)

