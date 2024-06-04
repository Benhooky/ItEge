s="С"*50 + "Г"*50 + "Н"*50
while "ГС" in s or "НС" in s or "ГН" in s:
    if "ГС" in s:
        s=s.replace("ГС","СГ")
    if "НС" in s:
        s=s.replace("НС","СН")
    if "ГН" in s:
        s=s.replace("ГН","НГ")
    print(s)