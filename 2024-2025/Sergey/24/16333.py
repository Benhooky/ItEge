f=open("ItEge/2024-2025/Sergey/24/24_16333.txt").readline()
maxLen=0
buffer=""
letters=["Q","R","W"]
digits=["1","2","4"]
for elem in f:
    buffer+=elem
    if len(buffer)>=2:
        if buffer[-1] in letters and buffer[-2] in letters or buffer[-1] in digits and buffer[-2] in digits:
            maxLen=max(maxLen, len(buffer)-1)
            buffer=buffer[-1]
print(maxLen)
