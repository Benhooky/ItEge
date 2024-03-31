s="123ab1ab3"
print(s.count("1"))
if "a" in s:
    print(1)
s = s.replace('a','b')#заменит все (a)
s = s.replace('a','b',1)#заменит только 1 (а)