from ipaddress import *
net = ip_network("253.112.169.12/255.255.254.0",strict=False)
cnt=0
for ip in net:
    binIp=f"{ip:b}"
    if binIp[:17].count("1") <= binIp[16:].count("1"):
        cnt+=1
print(cnt)