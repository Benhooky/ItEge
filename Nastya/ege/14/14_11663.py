from string import ascii_uppercase, digits
alph = digits + ascii_uppercase
alph = alph[:27]
for x in alph:
    result = int(f"17{x}35", 27) + int(f"{x}742M", 27) + int(f"{x} ", 27) ** 3
    if result % 23 == 0:
        print(result // 23)