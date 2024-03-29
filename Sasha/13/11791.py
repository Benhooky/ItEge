from ipaddress import *
cnt = 0
for A in range(0,9):
    net = ip_network(f'246.51.128.202/{16+A}', strict = False)
    #1
    # if all(f'{ip:b}'[:16].count('0')>f'{ip:b}'[16:].count('0') for ip in net):
    #     cnt+=1
    #2
    flag = True
    for ip in net:
        binIp = f'{ip:b}'
        if binIp[:16].count('0')>binIp[16:].count('0'):
            flag=False
            break
    if flag:
        print(A)