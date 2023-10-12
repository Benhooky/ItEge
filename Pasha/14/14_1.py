
# не рабочее если x > 35
def ten(str_to_convert: str, number: int) -> int:
    str_to_convert = str_to_convert[::-1]
    result = 0
    for index, value in enumerate(str_to_convert):
        result += int(value, 36) * number ** index
    return result


alphabet = [str(x) for x in range(0, 10)]+[chr(x)
                                           for x in range(ord('A'), ord('Z')+1)]
for x in alphabet[::-1]:
    if (ten('51' + x + '29', 150) + ten(x + '023', 150)) % 149 == 0:
        print((ten('51' + str(x) + '29', 150) + ten(str(x) + '023', 150)) // 149)
        break

# рабочее

for x in range(149, -1, -1):
    if ((5*150**4+1*150**3+x*150**2+2*150**1+9)+(x*150**3+2*150**1+3)) % 149 == 0:
        print(((5*150**4+1*150**3+x*150**2+2*150**1+9) +
              (x*150**3+2*150**1+3)) // 149, x)
        break
