maxD=0
num = int(input())
for i in range(num):
    b = int(input())
    if b%10==3:
        maxD = max(b,maxD)
print(maxD)