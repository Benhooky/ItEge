from fnmatch import fnmatch
for i in range(2658, 10**9+1, 2658):
    if fnmatch(str(i), '85?16*4'):
        print(i, i//2658)