from ipaddress import *
for mask in range(0,33):
    net = ip_network(f'173.103.25.118/{mask}',strict=False)
    if net.network_address == ip_address('173.103.24.0'):
        print(mask)