my_numbers = [int(x) for x in open("ItEge/Ksusha/17/17_11481.txt")]
max8 = 0
minSum = 1000000000000000
cnt = 0

for x in my_numbers:
    if str(x)[0] == "8":
        max8 = max(max8, x)

for i in range(len(my_numbers) - 2):
    cnt6 = 0
    if str(abs(my_numbers[i]))[0] == "6":
        cnt6 += 1
    if str(abs(my_numbers[i + 1]))[0] == "6":
        cnt6 += 1
    if str(abs(my_numbers[i + 2]))[0] == "6":
        cnt6 += 1
    if my_numbers[i] + my_numbers[i + 1] + my_numbers[i + 2] >= max8 and cnt6 <= 1:
        cnt += 1
        minSum = min(minSum, my_numbers[i] + my_numbers[i + 1] + my_numbers[i + 2])
print(cnt, minSum)
