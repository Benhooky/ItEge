from ipaddress import *
for A in range(8):
    net=ip_network(f'152.65.245.132/{16+A}',strict=False)
    Flag=True
    for ip in net:
        binIp=f'{ip:b}'
        if binIp[:16].count('0')<binIp[16:].count('0'):
            Flag=False
            break
    if Flag:
        print(A)
        
from ipaddress import *
for A in range(8):
    net=ip_network(f'152.65.245.132/{16+A}',strict=False)
    if all(f'{ip:b}'[:16].count('0')>=f'{ip:b}'[16:].count('0') for ip in net):
        print(A)