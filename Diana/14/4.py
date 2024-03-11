for x in range(8):
    flag = True
    for y in range(8):
        value = int(f'{x}01{y}4',9)+int(f'{x}{y}544',8)
        if value%89==0:
            print(value//89)
            flag = False
            break
    if not flag:
        break