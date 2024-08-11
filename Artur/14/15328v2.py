from string import digits, ascii_uppercase 
for x in (digits + ascii_uppercase)[:27]:
    a = int(f'123{x}24', 27) + int(f'135{x}78', 27)
    if a % 26 == 0:
        print(a // 26, x)