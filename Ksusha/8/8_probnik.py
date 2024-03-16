from itertools import product
lis = ["".join(x) for x in product('01234',repeat=5) if x[0]!='0']
answer = set()
for A in lis:
    for B in lis:
        answer.add(abs(int(A,5)-int(B,5)))
print(len(answer))