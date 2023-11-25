def is_Prime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


minSum = 1000000000
troy = 0
my_n = [int(x) for x in open("ItEge/Ksusha/17/17_10771.txt")]

for x in range(len(my_n) - 2):
    if str(my_n[x]).count("3") > 0:
        if str(my_n[x + 1]).count("3") > 0:
            if str(my_n[x + 2]).count("3") > 0:
                if is_Prime(my_n[x] + my_n[x + 2] + my_n[x + 1]):
                    minSum = min(minSum, my_n[x] + my_n[x + 2] + my_n[x + 1])
                    troy += 1
print(troy, minSum)
