from fnmatch import fnmatch
for i in range(2024,10**10+1,2024):
    if i**0.5 == int(i**0.5):
        if fnmatch(str(i),'1?2*4'):
            print(i,i//2024)