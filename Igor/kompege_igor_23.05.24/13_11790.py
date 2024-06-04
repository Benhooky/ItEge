from ipaddress import *
listA=[]
for A in range(16,25):
    flag=True
    net = ip_network(f"152.65.245.132/{A}",strict=False)
    for ip in net:
        binIp=f"{ip:b}"
        if not(binIp[:16].count("0")>=binIp[16:].count("0")):
            flag=False
            break
    if flag:
        listA.append(A)
print(min(listA)) 