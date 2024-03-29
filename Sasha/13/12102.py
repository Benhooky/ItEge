from ipaddress import *
for mask in range(33):
    net = ip_network(f'175.184.48.0/{mask}',strict=False)
    ip_uzel = ip_address('175.184.52.103')
    if ip_uzel in net:
        print(mask)