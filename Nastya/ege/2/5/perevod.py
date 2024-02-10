N = 100
s = ''
while N>0:
    s = str(N%4) + s
    N//=4
print(s)