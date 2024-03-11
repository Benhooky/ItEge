from string import digits,ascii_uppercase
for x in (digits+ascii_uppercase)[:19]:
    value = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
    if value % 18 == 0:
        print(value // 18)
