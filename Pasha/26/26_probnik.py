f = open('ItEge/Pasha/26/26_11681.txt')
n, k = map(int, f.readline().split())
s = sorted([list(map(int, x.split())) for x in f.readlines()], key=lambda y:y[0] * (y[1] / 100), reverse=True)
s1 = sorted([list(map(int, x.split().copy()) for x in f.readlines())],key= lambda x:x[2],reverse=True)
pass