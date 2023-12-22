
from functools import lru_cache
def F(n: int, current: list) -> int:
    if n < 3:
        return 2
    if n > 2 and n % 2:
        return 2*current[n-1]+current[n-2]-2
    else:
        return 2*current[n-2]-current[n-1]+2
@lru_cache()
def F_with_Opt(n):
    if n < 3:
        return 2
    if n > 2 and n % 2:
        return 2*F_with_Opt(n-1)+F_with_Opt(n-2)-2
    else:
        return 2*F_with_Opt(n-2)-F_with_Opt(n-1)+2
current = []
for i in range(171):
    current.append(F(i, current))
print(current[-1])
print(F_with_Opt(170))
