for x in "012345678":
    for y in "012345678":
        sum1 = int(f'88{x}4{y}', 9) + int(f'7{x}44{y}', 11)
        if sum1 % 61 == 0:
            print(sum1//61)
            break
