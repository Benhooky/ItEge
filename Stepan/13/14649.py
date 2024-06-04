from ipaddress import *

for A in range(256):
    net = ip_network(f'116.242.{A}.26/255.255.255.224', strict = False)
    if all(f"{ip:b}"[:16].count("1") >=f"{ip:b}"[16:].count("1") for ip in net ):
        print(A)