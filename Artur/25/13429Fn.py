from fnmatch import fnmatch

for i in range(83,10**6+1,83):
    if fnmatch(str(i),'1*578*'):
        print(i,i//83)