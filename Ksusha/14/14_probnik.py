from string import ascii_uppercase,digits
alph = digits+ascii_uppercase
def f(value,system):
    s = ''
    while value>0:
        s = alph[value%system]+s
        value//=system
    return s
for N in range(2,36):
    result = N**25-2*N**13+10
    result = f(result,N)
    sum1 = 0
    for i in result:
        sum1+=int(i)
    if sum1==75:
        print(N)
        break