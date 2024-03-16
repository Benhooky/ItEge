from string import ascii_uppercase,digits
for x in (digits+ascii_uppercase)[:19]:
    f = int(f'78{x}79643',19)+int(f'25{x}43',19)+int(f'63{x}5',19)
    if f%18==0:
        print(f//18)