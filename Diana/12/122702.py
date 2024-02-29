for i in range(300, 209, -1):
    N = "3" + "7" * i
    while ("27" in N) or ("377" in N) or ("777" in N):
        if "27" in N:
            N = N.replace("27", "32", 1)
        elif "377" in N:
            N = N.replace("377", "27", 1)
        elif "777" in N:
            N = N.replace("777", "3", 1)
    sum1 = sum(int(i) for i in N)
    if sum1 % 15 == 0:
        print(i)
