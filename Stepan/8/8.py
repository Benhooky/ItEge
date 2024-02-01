count = 0
for i in range(1000000, 10000000):
    octal = oct(i)[2:]
    if '3' not in octal:
        for d in range(6):
            if int(octal[d]) % 2 == 0 and int(octal[d+1]) % 2 == 0:
                count += 1
                break

print(count)
