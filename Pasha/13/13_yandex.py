from ipaddress import *
ip_add = ip_address('20.24.96.0')
for mask in range(21,33):
    ip_net = ip_network(f'{ip_add}/{mask}')
    if ip_address('20.24.110.42') in ip_net:
        print(mask)