def f(fram,too):
    while fram != too:
        if fram == too:
            return 1
        else:
            return f(fram*3,too) + f(fram-3,too)
print(f(3,30))