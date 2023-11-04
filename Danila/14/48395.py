for x in "0123456789AB":
    sum1 = int(f'28{x}2', 18)+int(f'93{x}5', 12)
    if sum1 % 133 == 0:
        print(sum1//133)
        break
