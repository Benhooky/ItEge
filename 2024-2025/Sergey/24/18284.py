f=open("ItEge/2024-2025/Sergey/24/24_18284.txt").readline()
buffer = ''
minLen = 1000000000
for elem in f:
    buffer += elem
    while buffer[0]!='L':
        buffer = buffer[1:]
        if len(buffer)==0:
            break
    if buffer.find('L')<buffer.find('O')<buffer.find('V')<buffer.find('E'):
        minLen = min(minLen,len(buffer[:buffer.find('E')+1]))
        buffer = buffer[1:]
print(minLen)