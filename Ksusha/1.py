ourList = [3, 4, 6, 7, 12, 432, 4]
ourList.append(2)
ourList.remove(4)
ourList.pop(1)
ourList.index(432)
ourList.insert(2, 3)
print(ourList)

ourStr = "2342552"
ourStr = ourStr[1:]
ourStr = ourStr[:3]+"5"+ourStr[3:]
print(ourStr)
print("".join(str(x) for x in ourList))
ourStr.count("5")
ourStr.strip(" 423 23 5354 5646 6455757")
ourStr = ourStr.replace("23", "")
ourStr.find("234")

a = (True, "234", 123, 432.123, 234)  # tuple / кортеж
b = a[0]
x1, x2, x3, x4, x5 = a


ourDict = {"key1": 100, "key2": 200}  # dict / словарь / hashTable
ourDict["key1"]  # 100
