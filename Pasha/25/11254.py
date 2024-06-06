from fnmatch import fnmatch
for x in range(5716,10**10+1,5716):
    if fnmatch(str(x),'56*139?4'):
        print(x,x//5716)