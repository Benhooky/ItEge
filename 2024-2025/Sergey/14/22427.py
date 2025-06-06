from string import ascii_uppercase,digits
alph=(digits+ascii_uppercase)[:14]
for x in alph:
    f=int(f"4B3{x}1C7",14) + int(f"5{x}G83F7",17)
    if f%15==0:
        print(f//15)
        break