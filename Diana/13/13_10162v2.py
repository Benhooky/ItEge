from ipaddress import *
ip1= '112.117.107.70'
ip2= ip_address('112.117.121.80')
for mask in range(32,15,-1):
    net = ip_network(f'{ip1}/{mask}',strict = False)
    if ip2 in net:
        print(mask)
        break