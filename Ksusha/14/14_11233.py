a_code = ord('A')
for x in range(26):
    if x > 9:
        x = chr(a_code + x - 10)
    m = (
        int(f"27{x}98876", 26)
        + int(f"26{x}51", 26)
        + int(f"15{x}47", 26)
        + int(f"62{x}5", 26)
    )
    if m % 25 == 0:
        print(m // 25, x)
        break
