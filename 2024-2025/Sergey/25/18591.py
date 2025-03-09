from fnmatch import fnmatch
for i in range(1984,10**10+1,1984):
    for Ч in range(0,10,2):
        for Н in range(1,10,2):
            if fnmatch(str(i),f'1{Ч}3*4?{Н}'): 
                print(i,i//1917)