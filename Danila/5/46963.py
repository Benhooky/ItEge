
for n in range(2,10000):
    s = bin(n)[2:]
    cnt0 = 0
    cnt1 = 0
    for i in range (len(s)):
        if (i+1) % 2 == 0 and s[i] == "1":
            cnt1 += 1
        elif (i+1) % 2 != 0 and s[i] == "0":
            cnt0 += 1
    if (R:=abs(cnt1 - cnt0)) == 5:
        print(n)
        break