for n in range(4, 1000):
    s = "2" + "5" * n
    while ("25" in s) or ("35" in s) or ("555" in s):
        if "25" in s:
            s = s.replace("25", "53", 1)
        if "35" in s:
            s = s.replace("35", "2", 1)
        if "555" in s:
            s = s.replace("555", "23", 1)
    sum_s = 0
    for l in s:
        sum_s += int(l)
        if sum_s > 7:
            break
    if sum_s % 7 == 0:
        print(n)
        break