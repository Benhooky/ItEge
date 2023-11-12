for x in range(1,1000):
    n = 4*625**1920+4*125**x-4*25**1940-3*5**1950-1960
    s = ""
    while n>0:
        s+=str(n%5)
        n//=5
    s=s[::-1]
    if s.count("0")==1891:
        print(x)
        break