from string import ascii_uppercase
f = open('ItEge/Ksusha/24/24_2508.txt')
SmaxQ = ''
maxQ = 0
for string in f:
    string=string[:-1]
    if maxQ <= string.count('Q'):
        maxQ = max(maxQ, string.count('Q'))
        SmaxQ = string
#1 Dictionary
answer = {x:SmaxQ.count(x) for x in ascii_uppercase}
mostRare = 1000000
rareLat = ''
for pair in answer.items():
    if mostRare > pair[1]:
        rareLat = pair[0]
        mostRare = pair[1]
print(answer)
print(rareLat)
#2 Key
print(min(SmaxQ, key=lambda x: SmaxQ.count(x)))
