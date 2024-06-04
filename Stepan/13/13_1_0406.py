from ipaddress import *
for mask in range(1,33):
    net = ip_network(f'175.122.80.0/{mask}',0)
    cntuzel = 0
    if ip_address('175.122.80.13') in net.hosts():
        for ip in net.hosts():
            cntuzel+=1
            if cntuzel>=60:
                print(mask)
                break