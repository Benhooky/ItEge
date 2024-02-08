for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s += "00"
    else:
        s += "11"
    if int(s, 2) > 115:
        print(n)
        break
