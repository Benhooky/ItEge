alph = '0123456789ABCDEF'
answer = set()
for x in alph:
    for y in alph[9:]:
        if int(x, 16) < int(y, 16):
            result = int(f'5{x}{y}C', 16) + int(f'8{x}{x}7', alph.index(y))
            answer.add(result)
print(len(answer))