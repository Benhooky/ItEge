from fnmatch import fnmatch
for i in range(7777, 10**10+1, 7777):
    if fnmatch(str(i), '12*567?'):
        print(i, i//7777)