from ipaddress import *
for mask in range(32):
    net1 = ip_network(f'84.77.47.132/{mask}', 0)
    net2 = ip_network(f'84.77.48.132/{mask}', 0)
    if net1!=net2:
        print(mask)