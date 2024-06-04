from ipaddress import *
cnt = 0
for A in range(0, 256):
    flag = True
    net = ip_network(f'246.81.65.{A}/255.255.255.224', strict = False)
    for ip in net.hosts():
        binIp = f'{ip:b}'
        if binIp[16:24].count('0') <= binIp[24:].count('0'):
            flag = False
            break
    if flag:
        cnt+=1
print(cnt)