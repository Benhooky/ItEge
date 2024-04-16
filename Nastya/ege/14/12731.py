from string import ascii_uppercase,digits
alph = digits + ascii_uppercase
alph = alph[:13]
for x in alph:
    result = int(f'9{x}AB',13)+int(f'{x}46C',16)-int(f'B7{x}',16)
    if result%14==0:
        print(result/14)