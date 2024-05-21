from string import ascii_uppercase, digits
alphabet=digits + ascii_uppercase
maxValue = 0
result = 0
for y in alphabet[9:14]:
    for x in alphabet[alphabet.index(y)+1:14]:
        value= int(f'7{x}37{y}',14)+ int(f'9{y}63',alphabet.index(x))-int('15148',alphabet.index(y))
        if value>maxValue:
            result=value//(alphabet.index(x)+alphabet.index(y))
            maxValue = value
print(result)