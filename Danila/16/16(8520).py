def F(n):
    if n >= 2025:
        return n
    else:
        return n + 3 + F(n + 3)
        
print(F(2018) - F(2022))