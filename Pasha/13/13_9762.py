from ipaddress import *
for mask in range(0, 33):
    net = ip_network(f'111.81.192.0/{mask}', strict=False)
    if ip_address('111.81.208.27') in net:
        print(mask)