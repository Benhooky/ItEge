from ipaddress import *
for mask in range(16,25):
    net = ip_network(f"238.51.1.202/{mask}",strict=False)
    flag=True
    for ip in net:
        binIp=f"{ip:b}"
        if (binIp[:16].count("1")<binIp[16:].count("1")):
            flag=False
            break
    if flag:
        print(net.netmask)