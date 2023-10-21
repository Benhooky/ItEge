for n in range(2, 1000):
    i = bin(n)[2:]  # 10
    digits_to_add = i[1] * 2  # 00
    i = i[:-1] + digits_to_add  # 100
    r = int(i, 2)
    if r > 92:
        print(n)
        break
