f=open("ItEge/2024-2025/Sergey/24/24_13100.txt").readline()
maxLen=0
buffer=""
for elem in f:
    buffer+=elem
    if buffer.count("C")==3 or buffer.count("D")==3:
        maxLen=max(maxLen,len(buffer)-1)
        buffer=buffer[buffer.index(elem)+1:]
print(maxLen)