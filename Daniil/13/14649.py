from ipaddress import *
for A in range(256):
    net1 = ip_network(f'116.242.{A}.26/255.255.255.224',strict = False)
    flag = True
    for ip in net1:
        binIp = f'{ip:b}'
        if binIp[:16].count('1')<binIp[16:].count('1'):
            flag=False
            break
    if flag:
        print(A)