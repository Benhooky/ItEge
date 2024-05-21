from itertools import permutations


# Генерация всех перестановок из строки 'abc'
perms = permutations('abc')


# Вывод перестановок
for perm in perms:
    print(''.join(perm))