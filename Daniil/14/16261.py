from string import digits,ascii_uppercase
alph = (digits+ascii_uppercase)[:21]
for x in alph:
    for y in alph: 
        res =  int(f'943697{x}21',21)-int(f'2{y}9253',21)
        if res%20==0:
            print(res//20,int(f'{x}',21)-int(f'{y}',21))
