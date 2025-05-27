from fnmatch import fnmatch
for i in range(2023,10**9,2023):
    if (i % 19 == 0) and (i % 6 == 0):
        if fnmatch(str(i),"1*1*1?"):
            print(i)