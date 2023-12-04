for n in range(4,100):
    s = '2' + '5' * n
    while ('25' in s) or ('355' in s) or ('555' in s):
        s = s.replace('25', '5', 1)
        s = s.replace('355', '52', 1)
        s = s.replace('555', '3', 1)
    if 2*s.count("2")+3*s.count("3")+5*s.count("5") == 17:
        print(n)
        break