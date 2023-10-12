def R(s1,file):
    if s1+"PC" in file:
        s1+="PC"
        R(s1,file)
        return s1
    if s1+"CSGO" in file:
        s1+="CSGO"
        R(s1,file)
        return s2

s1="PC"
s2="CSGO"
file=open("Misha/24_9552 (1).txt").readline()[:-1]
print(max(len(R(s1,file))),())
s="AOAOAOAOBKBKBKBBKKBAOAOAOAOABBKBKBKBKBKBKBKBAO"
s=s.replace("AO","1")
s=s.replace("BK","1")

print(s)
k="1"

