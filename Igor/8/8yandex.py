import itertools
S = ["".join(x) for x in itertools.product("АЕКПТЧ",repeat=7)]
print((S.index("ПЕЧАТКА")) - (S.index("АПТЕЧКА"))-1)