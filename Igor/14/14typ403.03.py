n=2*729**333+2*243**334-81**335+2*27**336-2*9**337-338
s=""
while n>0:
    s+=str(n%9)
    n//=9
print(len(s)-s.count("0"))