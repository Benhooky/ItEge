S=open('24(4)(21.05).txt').readline()[:-1]
answer="XYZ"
while answer in S:
    answer+="XYZ"
while answer not in S:
    answer=answer[:-1]
print(answer)