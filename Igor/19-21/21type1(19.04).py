def f(first, second, third, turn):
    if first+second+third>=25:
        if turn==2 or turn==4:
            return True
        else:
            return False
    if turn > 4:
        return False
    else:
        if turn%2==0: #peta
            return (
                f(first+2, second+2, third+2, turn+1) and 
                f(first*2, second, third, turn+1) and
                f(first, second*2, third, turn+1) and
                f(first, second, third*2, turn+1)
            )
        else:
            return (
                f(first+2, second+2, third+2, turn+1) or 
                f(first*2, second, third, turn+1) or
                f(first, second*2, third, turn+1) or
                f(first, second, third*2, turn+1)
            )
for S in range(1,19):
    if f(2,3,S,0):
        print(S)