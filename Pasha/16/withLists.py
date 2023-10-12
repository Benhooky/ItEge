

def F(n: int, current: list) -> int:
    if n < 3:
        return 2
    if n > 2 and n % 2:
        return 2*current[n-1]+current[n-2]-2
    else:
        return 2*current[n-2]-current[n-1]+2


current = []
for i in range(171):
    current.append(F(i, current))
print(current[-1])
