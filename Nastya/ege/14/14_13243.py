from string import ascii_uppercase,digits
alph = digits + ascii_uppercase
alph = alph[:18]
for x in alph:
    result = (int(f'1{x}253',18) + int(f'32{x}8',18))
    if result % 7 == 0:
        print(result // 7)# ответ 19367