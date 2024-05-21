from ipaddress import *
for mask in range(16,25):
    net = ip_network(f'246.51.128.202/{mask}',strict=False)
    flag = True
    for ip in net:
        binIp = f'{ip:b}'
        if binIp[:16].count('0')>binIp[16:].count('0'):
            flag=False
            break
    if flag:
        #print(net.netmask)
        print(mask)
        break