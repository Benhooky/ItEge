from fnmatch import fnmatch
for i in range(3377,10**10+1,3377):
    if fnmatch(str(i),'?79?8*3'):
        if (1+i)%2==1:
            print(i,i//3377)