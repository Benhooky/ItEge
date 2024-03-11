def treug(n,m,k):
    l = sorted([n,m,k])
    if l[0]+l[1]>l[2]:
        return True
    return False
