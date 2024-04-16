from string import digits, ascii_uppercase
alphavit = (digits + ascii_uppercase)[:16]
for y in alphavit:
    for x in alphavit:
        otv = int(f'27A{x}23', 16) + int(f'8{y}E5D2', 16)
        if otv % 5 == 0:
            print(int(x, 16) + int(y, 16))