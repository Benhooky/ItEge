from string import digits,ascii_uppercase
alph = (digits+ascii_uppercase)[:18]
for x in alph:
    res = int(f'71{x}264',18)+int(f'4{x}51',18)+int(f'21{x}637',18)
    if res%17==0:
        print(res//17)