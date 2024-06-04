from fnmatch import fnmatch
for i in range(206,10**13,206):
    if fnmatch(str(i),"12?345?67089?"):
        print(i,i//206)