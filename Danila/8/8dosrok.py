from itertools import product
a = product("АПРСУ", repeat=5)
words = ["".join(x) for x in a]
number = 0
for my_str in words:
    number += 1
    if (my_str.count("У")<=1) and "АА" not in my_str:
        print(number)
        break