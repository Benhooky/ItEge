f = open('ItEge/Pabufferha/24/24_11667.txt').readline()
buffer = ''
mx = 0
for i in range(len(f)):
    buffer += f[i]
    if buffer.count('INFINITY') == 1001:
        mx = max(mx, len(buffer) - 1)
        buffer = buffer[buffer.index('INFINITY') + 1:]
print(mx)