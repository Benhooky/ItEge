d1 = {1:[1,2,3],2:[-2,1],3:[2,5,1,1,1]}
b = dict(sorted(d1.items(),key=lambda x: len(x[1])))
print(b)