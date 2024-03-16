def F(x):
    return all(x % d for d in range(2, int(x**0.5)+1))
ct= sum(F(a) for a in range(1, 11111))
print(ct)