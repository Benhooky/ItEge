file=open("Kate/24_9552.txt").readline()[:-1]
PC=file
PC=PC.replace("PC","1")
PC=PC.replace("CSGO","11")
CSGO=file
CSGO=CSGO.replace("CSGO","11")
CSGO=CSGO.replace("PC","1")
sPC="1"
sCSGO="1"
while sPC+"1" in PC:
    sPC+="1"
while sCSGO+"1" in CSGO:
    sCSGO+="1"
print(2*max(len(sPC),len(sCSGO)))
