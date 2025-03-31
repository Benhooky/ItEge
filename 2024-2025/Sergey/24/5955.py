f=open("ItEge/2024-2025/Sergey/24/24_5955.txt").readline()
maxLen=0
buffer=""
masGlas="AO"
masSogl="CDF"
for elem in f:
    buffer+=elem
    if len(buffer)>=4:
        if buffer[-4] in masSogl and buffer[-3] in masGlas and buffer[-2] in masGlas and buffer[-1] in masSogl:
            maxLen=max(maxLen,len(buffer)-1)
            buffer=buffer[-3:]
print(maxLen)