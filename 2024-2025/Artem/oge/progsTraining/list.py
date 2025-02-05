masiv = [3,5,7,8,5,7]
print(masiv[-1])
masiv.append(2) # добавление
print(masiv)
masivOdn = [2,2]
print(masivOdn[1])
masivDv = [[2,2],[3,3,5,7]]
print(masivDv[1][2])
masivDv[1].pop(-1) # удаление по индексу
print(masivDv)

phoneBook = ["Иванов", "Смирнов", "Соболев", "Щербаков"]
phoneBook.sort()
#print(phoneBook.pop(-1))
phoneBook.remove("Щербаков") # удаление по значению
print(phoneBook)
phoneBook.insert(1, "Запашный") # для вставки по индексу
print(phoneBook)
phoneBook[2] = "Соловьев"
print(phoneBook)