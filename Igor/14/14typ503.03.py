n=361*2349**84-89**192+1953**481*4843**151
s=""
while n>0:
    s+=str(n%9)
    n//=9
print(s.count("5"))