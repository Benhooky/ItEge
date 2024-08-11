# for x in range (10000):
#     if 10*x%8==0:
#         i = 10*x//8
#     else:
#         i = 10*x//8+1 
#     if 862*i <= 276*1024:
#         print(x)

for i in range(10000):
    if 261 * i % 8 == 0:
        x = 261 * i // 8
    else:
        x = 261 * i // 8 + 1
    if x > 128.73606:
        print(i)
        break
