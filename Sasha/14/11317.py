from string import digits, ascii_uppercase
for x in (digits+ascii_uppercase)[:17]:
    f = int(f'7AC{x}53D', 17) + int(f'83BG94{x}D', 17) + int(f'C5{x}D', 17) + int(f'C4BBF{x}4', 17) + int(f'7{x}79', 17)
    if f%16 == 0:
        print(f//16)