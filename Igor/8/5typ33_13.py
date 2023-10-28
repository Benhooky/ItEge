A = "0123456789ABC"
for x in A:
    for y in A:
        f = int(f"8{x}78{y}", 13) + int(f"79{x}{y}7", 18)
        if f % 9 == 0:
            print(f//9)
            break
