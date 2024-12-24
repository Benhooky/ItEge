for n in range (1,1000):
    s = '3'*15+'2'*18+'1'*n
    while '31' in s or '33' in s or '21' in s:
        if '31' in s:
            s = s.replace('31','123',1)
        if '33' in s:
            s = s.replace('33','211',1)
        if '21' in s:
            s = s.replace('21','1',1)
    sum0 = 0
    for el in s:
        sum0 += int(el)
    if sum0>24:
        print(n)
        break