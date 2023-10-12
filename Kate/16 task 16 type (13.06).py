answer=[0]*4044
def H(x,answer):
    if x>=4040:
        return x
    if x<4040:
        return x+4+answer[x+4]
for i in range (len(answer)-1,0,-1):
    answer[i]=H(i,answer)
print(answer[3]-answer[15])