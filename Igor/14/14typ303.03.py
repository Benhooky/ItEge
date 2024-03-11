from string import digits,ascii_uppercase
for x in (digits+ascii_uppercase)[:19]:
    s = int(f'78{x}79643',19) + int(f"25{x}43",19) + int(f"63{x}5",19)
    if s%18==0:
        print(s//18)