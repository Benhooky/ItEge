f = open('ItEge/2024-2025/Sergey/24/24_17641 (2).txt').readline()
maxLen=0
buffer=""
activeDigit = False
for elem in f:
    buffer+=elem
    if '++' in buffer or '*+' in buffer or '+*' in buffer or '**' in buffer:
    if elem != '0' and elem != '+' and elem != '*':
        activeDigit = True
        
print(maxLen)