from ipaddress import *
net = ip_network('112.154.132.0/255.255.252.0',strict = False)
cnt = 0
for ip in net.hosts():
    l = f"{ip:b}"[:16]
    r = f"{ip:b}"[16:]
    if (l.count("1") <= r.count("0")) and r.count("0") % 2 == 1:
        cnt +=1
print(cnt)