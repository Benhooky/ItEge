import itertools
alph = "ABCX"
s = itertools.product(alph, repeat=5)
st = []
for i in s:
    st.append("".join(list(i)))
ct = 0
for r in st:
    if r.count("X") == 0:
        ct += 1
    elif r.count("X") == 1 and r[0] == "X":
        ct += 1
print(ct)
