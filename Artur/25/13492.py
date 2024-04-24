from fnmatch import fnmatch
for i in range(23, 10**6 + 1, 23):
    maxDel = 0
    for x in range(2, int(i ** 0.5) + 1):
        if i%x == 0:
            maxDel = max(maxDel, i//x)
    if fnmatch(str(maxDel), '*6215'):
        print(i, maxDel)