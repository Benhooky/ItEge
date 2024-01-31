from ipaddress import *
for A in range(256):
    net = ip_network(f'183.192.{A}.0/255.255.252.0',strict = False)
    flag = True
    for ip in net:
        bin_ip = f'{ip:b}'
        bin_ip = bin_ip[16:]
        if bin_ip.count('1')<=3:
            flag = False
            break
    if flag:
        print(A)
        break