cntNotServed = 0
clientsInTwo = 0
def placePersonToQueue(queues:dict,person:list,cntNotServed:int,clientsInTwo=clientsInTwo):
    if len(queues[person[2]]) >= 14:
        cntNotServed += 1
    else:
        queues[person[2]].append(queues[person[2]][-1] + person[1])
        if person[2]==2:
            clientsInTwo += 1
        cntToLeave = sum(1 for x in queues[person[2]] if x < person[0])
        for j in range(cntToLeave):
            queues[person[2]].pop(0)
f = open('ItEge/Pasha/26/26_13101.txt')
n = int(f.readline())
s = sorted([[x for x in map(int, i.split())] for i in f.readlines()], key=lambda y:y[0])
queues = {1:[], 2:[]}
while len(queues[1])==0 and len(queues[2])==0:
    
for person in s:
    if person[2] == 0:
        if len(queues[1]) <= len(queues[2]):
            placePersonToQueue(queues[1],person,cntNotServed)
        else:
            placePersonToQueue(queues[2],person,cntNotServed)
    elif person[2]==1:
        placePersonToQueue(queues[1],person,cntNotServed)
    else:
        placePersonToQueue(queues[2],person,cntNotServed)
print(clientsInTwo, cntNotServed)