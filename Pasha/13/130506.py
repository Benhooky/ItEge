from ipaddress import *
mn = 100000000000
for A in range(16,25):
    ip_net = ip_network(f'238.51.1.202/{A}', strict=False)
    flag = True
    for ip in ip_net:
        ip = f'{ip:b}'
        if ip[:16].count('1') < ip[16:].count('1'):
            flag = False
            break
    if flag:
        print(ip_net.netmask)