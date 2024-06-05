from ipaddress import *
ip1= ip_address('112.117.107.70')
ip2= ip_address('112.117.121.80')
for mask in range(32,15,-1):
    net = ip_network(f'{ip2}/{mask}',strict = False)
    if ip1 == net.network_address:
        print(net.netmask)