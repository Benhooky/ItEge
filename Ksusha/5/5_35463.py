for n in range(100,10000):
    dv=bin(n)[2:]
    cnt1=dv.count('1')
    cnt0=dv.count('0')
    if cnt0==cnt1:
        dv+=dv[-1]
    elif cnt0>cnt1:
        dv+='1'
    else:
        dv+='0'
    cnt1=dv.count('1')
    cnt0=dv.count('0')
    if cnt0==cnt1:
        dv+=dv[-1]
    elif cnt0>cnt1:
        dv+='1'
    else:
        dv+='0'
    cnt1=dv.count('1')
    cnt0=dv.count('0')
    if cnt0==cnt1:
        dv+=dv[-1]
    elif cnt0>cnt1:
        dv+='1'
    else:
        dv+='0'
    r=int(dv,2)
    if r%4==0:
        print(n)
        break


