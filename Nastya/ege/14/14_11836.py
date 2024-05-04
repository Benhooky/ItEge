from string import ascii_uppercase, digits
alph = digits + ascii_uppercase
alph = alph[:32]
for x in alph:
    result = int(f"931{x}964", 32) + int(f"4{x}51{x}1", 32) + int(f"2861{x}637", 32)
    if result % 31 == 0:
        print(result // 31)#ответ 2820159444