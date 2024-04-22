from itertools import product
from string import digits,ascii_uppercase
alph = (digits+ascii_uppercase)[:14]
allNumbers = ["".join(x) for x in product(alph, repeat = 5)]
cnt = 0
for digit in allNumbers:
    print(digit)
    if len(set(digit))==2:
        if digit[-1]=='0' or digit[-1]=='3':
            if digit[0]!='0':
                cnt+=1
print(cnt)