maxres=0
for n in range(4,10000):
    s = "1"+n*"9"
    while "19" in s or "49" in s or "999" in s:
        if "19" in s:
            s=s.replace("19","9",1)
        if "49" in s:
            s=s.replace("49","91",1)
        if "999" in s:
            s=s.replace("999","4",1)
    res=0 
    for x in s:
        res+= int(x)
    maxres = max(maxres,res)
print(maxres)