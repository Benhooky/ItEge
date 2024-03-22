
from re import L


f = open('ItEge/Pasha/26/26_13101.txt')
n = int(f.readline())
s = sorted([[x for x in map(int, i.split())] for i in f.readlines()], key=lambda y:y[0])
pass
for t in range(10000):
    