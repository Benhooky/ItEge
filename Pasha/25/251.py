from fnmatch import fnmatch
for x in range(206,(10**13)+1,206):
    if fnmatch(str(x), '12?345?67089'):
        print(x,x//206)