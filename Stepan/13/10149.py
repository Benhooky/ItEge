from ipaddress import *
for mask in range(33):
    net = ip_network(f'220.128.112.142/{mask}', strict = False)
    if net.network_address == ip_address('220.128.96.0'):
        print(net.netmask)#19