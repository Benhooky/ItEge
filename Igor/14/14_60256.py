for x in '0123456789ABCDEFGHKLMNOPQ':
    sum1 = int('8'+x+'5678', 25)+int('457'+x+'69', 25)+int('145'+x+'1', 25)
    if sum1 % 23 == 0:
        print(sum1//23)
        break
