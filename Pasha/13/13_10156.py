from ipaddress import *
for mask in range(33):
    net = ip_network(f'203.155.64.98/{mask}', strict = False)
    if net.network_address == ip_address('203.155.64.0'):
        print(mask)