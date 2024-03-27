from ipaddress import *
ip = ip_address('175.184.52.103')
for i in range(32,-1,-1):
    net = ip_network(f'175.184.48.0/{i}',strict=False)
    if ip in net:
        print(i)
        break