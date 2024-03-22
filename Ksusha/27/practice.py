lis = [2,4,21,123,54,-52]
n = len(lis)
#O(n)
for i in range(len(lis)):
    print(i)
#O(nln(n))
for i in range(len(lis)-1):
    for j in range(i+1,len(lis)):
        print(i,j)
#O(n^2)
for i in range(len(lis)):
    for j in range(len(lis)):
        print(i,j)
#O(n^3)
for i in range(len(lis)):
    for j in range(len(lis)):
        for k in range(len(lis)):
            print(i,j,k)
#O(n)
for i in range(len(lis)):
    print(i)
for i in range(len(lis)):
    print(i)