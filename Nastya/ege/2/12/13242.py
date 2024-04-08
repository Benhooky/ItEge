s ="5"*874
while ("555" in s) or ("111" in s):
    if "555" in s:
        s = s.replace("555", "1",1)
    else:
        s = s.replace("111", "5",1)
print(s.count("5"))