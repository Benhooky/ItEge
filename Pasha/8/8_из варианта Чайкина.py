from itertools import permutations
s = '014689ACEFG'
print(len([''.join(x)
      for x in permutations(s, 6) if (x[0] != '0' and int(x[0], 17) % 2 == 0)]))
