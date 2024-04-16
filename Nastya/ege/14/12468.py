from string import ascii_uppercase,digits
alph = digits+ascii_uppercase
alph = alph[:19]
for x in alph:
    result = int(f"78{x}79643", 19)+int(f"25{x}43", 19)+int(f"63{x}5", 19)
    if result%18 ==0:
        print(result//18)