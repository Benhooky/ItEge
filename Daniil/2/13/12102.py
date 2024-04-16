from ipaddress import *
#net = ip_network('Адрес сети или узел/маска')
for mask in range(0,33):
    net = ip_network(f'175.184.48.0/{mask}',strict = False)
    uzel = ip_address('175.184.52.103')
    if uzel in net:
        print(mask)