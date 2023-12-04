from itertools import product

a = product("АГМНСТУ", repeat=6)

arl = ["".join(x) for x in a]

for word in arl[::-1]:
    if word[0] != "У" and word.count("М") == 2 and word.count("Г") <= 1:
        print(arl.index(word) + 1)
        break
