from fnmatch import *
def cntdel(a):
    cnt = 2
    for b in range(2, int(a ** 0.5) + 1):
        if a % b == 0:
            cnt += 2
    if a**0.5 == int(a**0.5):
        cnt-=1
    return cnt
for i in range(2031, 10 ** 9, 2031):
    if i % 31 == 0 and i % 2031 == 0:
        if fnmatch(str(i), '*31*65?'):
            ct = cntdel(i)
            while ct % 2 == 0:
                ct /= 2
            if ct == 1:
                print(i, i / 2031)