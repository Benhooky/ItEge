from ipaddress import *
for A in range (16,33):
    net=ip_network(f'187.124.21.237/{A}',0)
    flag = True
    for ip in net:
        if not(f'{ip:b}'[:16].count('1')>=f'{ip:b}'[16:].count('1')):
            flag = False
            break
    if flag:
        print(A)
        break
