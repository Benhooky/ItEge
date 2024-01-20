f = open("ItEge/Pasha/24/24_12111.txt").readline()
s = f.replace("HPY", "*")
s = f.replace("NYN", "*")
while s in f:
    s += "*"
print(len(s))