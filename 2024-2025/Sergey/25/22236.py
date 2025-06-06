def f(x):
    delit=set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            delit.add(i)
            delit.add(x//i)
    return sorted(delit)
for x in range(30000000,10000000000000):
    delit=f(x)
    minDel = 1000000000000000
    for z in delit:
        if z%1000==134:
            if z!=134:
                print(x,z)