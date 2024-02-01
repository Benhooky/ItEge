from ipaddress import *
min12=689587456736376
for a in range (32,0,-1):
    net1=ip_network(f'112.117.107.70/{a}',0)
    net2=ip_network(f'112.117.121.80/{a}',0)
    if net1==net2:
        ipCnt=0
        for ip in net1:
            ipCnt+=1
        print(ipCnt)
        break

