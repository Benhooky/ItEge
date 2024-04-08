from ipaddress import *
cntStr = 0
net = ip_network('203.111.195.0/255.255.240.0',strict = False)
for ip in net:
    binIp = f'{ip:b}'
    if binIp.count("0")%3==0:
        if "111" in binIp and "000" in binIp:
            cntStr += 1
print(cntStr)
