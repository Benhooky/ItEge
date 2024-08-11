for x in range(1,2031):
    s = 6**260+6**160+6**60-x
    system = 6
    answer = ''
    while s > 0:
        answer += str(s % system)
        s //= system
    #answer = reversed(answer)
    #answer.reverse()
    answer = answer[::-1]
    if answer.count('0')==202:
        print(x)