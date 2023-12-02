lis = open("ItEge/Ksusha/17/17.txt")
my_numbers = [int(x) for x in lis]
cntt = 0
maxKv = 1
naim = 100000000
for i in my_numbers:
    if (len(str(i)) == 3) and (str(i)[-1] == '5'):
        naim = min(naim, i)
for i in range(len(my_numbers) - 1):
    if (len(str(my_numbers[i])) == 4 and len(str(my_numbers[i + 1])) != 4) or (
        (len(str(my_numbers[i]))) != 4 and len(str(my_numbers[i + 1])) == 4
    ):
        if ((my_numbers[i] **2) + (my_numbers[i+1])**2) % naim == 0:
            cntt += 1
            maxKv = max(maxKv, (my_numbers[i] **2) + (my_numbers[i+1])**2)
print(cntt, maxKv)
