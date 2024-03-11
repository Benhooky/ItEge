from string import digits,ascii_uppercase
for x in (digits+ascii_uppercase)[:12]:
    for y in (digits+ascii_uppercase)[:12]:
        value = int(f'{x}231{y}', 12) + int(f'78{x}98{y}', 14)
        if value % 99 == 0:
            print(value // 99)
