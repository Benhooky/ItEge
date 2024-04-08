for n in range(9999, 3, -1):
    s = "5"+ n*"2"
    while ("52" in s) or ("2222" in s) or ("1122" in s):
        if "52" in s:
            s = s.replace("52", "11")
        if "2222" in s:
            s = s.replace("2222", "5")
        if "1122" in s:
            s = s.replace("1122", "25")
    sum_s = 0
    for l in s:
        sum_s += int(l)
        if sum_s>64:
            break
    if sum_s == 64:
        print(n)
        break
