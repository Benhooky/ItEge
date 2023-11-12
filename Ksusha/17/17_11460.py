f = open("ItEge/Ksusha/17/17_11460.txt")
my_numbers = [int(x) for x in f]
max8 = 0
cnt = 0
min_sum = 100000000000000
for i in my_numbers:
    if str(i)[0] == "8":
        max8 = max(max8, i)

for i in range(len(my_numbers) - 2):
    if (
        str(abs(my_numbers[i]))[0]
        + str(abs(my_numbers[i + 1]))[0]
        + str(abs(my_numbers[i + 2]))[0]
    ).count('6') <= 1:
        if my_numbers[i] + my_numbers[i + 1] + my_numbers[i + 2] >= max8:
            cnt += 1
            min_sum = min(
                min_sum, my_numbers[i] + my_numbers[i + 1] + my_numbers[i + 2]
            )
print(cnt, min_sum)
