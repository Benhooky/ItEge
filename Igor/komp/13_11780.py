from ipaddress import *
net = ip_network("185.8.0.0/255.255.128.0",strict=False)
cnt=0
listAnswer = []
for ip in net:
    binIp=f"{ip:b}"
    listAnswer.append(binIp.count('1'))
print(max(listAnswer))