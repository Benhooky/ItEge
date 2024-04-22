from ipaddress import *
for mask in range(1,33):
    net1 = ip_network(f'216.54.187.235/{mask}',strict = False)
    net2 = ip_network(f'216.54.174.128/{mask}',strict = False)
    cnt1=0
    cnt2=0
    for x in net1:
        cnt1+=1
        if cnt1>2:
            break
    for x in net2:
        cnt2+=1
        if cnt2>2:
            break
    if net1 != net2 and cnt1>=2 and cnt2>=2:
        print(mask)