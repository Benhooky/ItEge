from string import ascii_uppercase,digits
alph = (digits + ascii_uppercase)[:27]
for x in alph:
    sum1 = int(f'123{x}24',27)+int(f'135{x}78',27)
    if sum1%26 == 0:
        print(sum1//26)