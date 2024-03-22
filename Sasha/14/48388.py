from string import digits, ascii_uppercase
alph = (digits+ascii_uppercase)[:12]
for x in alph:
    for y in alph:
        s = int(f'{x}231{y}',12) + int(f'78{x}98{y}',14)
        if s%99 == 0:
            print(s//99)