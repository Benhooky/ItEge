from ipaddress import ip_network

for mask in range(16,25):
    flag=True
    net= ip_network(f"127.63.67.1/{mask}",strict=False)
    for ip in net:
        binIp=f"{ip:b}"
        if not(binIp[:16].count("1")>=binIp[16:].count("1")):
            flag=False
            break
    if flag:
        print(net.netmask)