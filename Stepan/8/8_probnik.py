from itertools import product
alph = ["А", "З", "И", "М", "Н", "О", "П", "Р", "Т"]
number = 0
for x in product(alph, repeat = 5):
    number+=1
    word = "".join(x)
    if number % 2 == 0:
        if x[0] == 'Н':
            if word.count('Р') == 2:
                print(number)