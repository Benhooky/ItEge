from ipaddress import *
for A in range(256):
    net = ip_network(f"183.192.{A}.0/255.255.252.0",strict=False)
    flag=True
    for ip in net:
        binIp = f'{ip:b}'
        if binIp[16:].count('1')<=3:
            flag=False
            break
    if flag:
        print(A)
        break

