from ipaddress import *
for A in range(255,-1,-1):
    flag = True
    net = ip_network(f'223.167.{A}.128/255.255.255.192',0)
    for ip in net:
        f=f'{ip:b}'
        if f[:16].count('0')>f[16:].count('0'):
            flag = False
            break
    if flag:
        print(A)
        break