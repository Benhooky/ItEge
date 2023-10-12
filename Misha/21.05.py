
def f(n,k):
    if n<k or n==50: return 0
    if n==k:return 1
    if n>k: return f(n-1,k)+f(n-4,k)+f(n//2,k)
print(f(100,73)*f(73,72)*f(72,2))
