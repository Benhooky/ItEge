def f(x,y,cnt):
    if x >= y: return x == y and cnt <= 2
    return f(x+1,y,cnt) + f(x+2,y,cnt) + f(x*2,y,cnt+1)
print(f(2,12,0))