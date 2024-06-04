from ipaddress import *
uzl = ip_address('175.122.80.13')
answerCnt = 0
for mask in range(1, 33):
    net = ip_network(f'175.122.80.0/{mask}', strict = False)
    cnt = 0
    if uzl in net:
        if len(list(net.hosts()))>=28:
            answerCnt+= 1
print(answerCnt)