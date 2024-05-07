from ipaddress import *
ip=ip_address('76.155.48.2')
cnt=0
for mask in range(33):
    net=ip_network(f'76.155.48.0/{mask}',strict = False)
    if ip in net:
        cnt+=1
print(cnt)