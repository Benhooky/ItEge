def f(x):
    delit=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            delit.add(i)
            delit.add(x//i)
    return sorted(delit)


res = f(100)
sum(res)
min(res)+max(res)

for x in res:
    if x%3==0:
        cnt+=1