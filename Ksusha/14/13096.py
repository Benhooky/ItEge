for x in range(39):
    for y in range(39):
        s = [5,8,x,7,2,3,y,4,9][::-1]
        sum1 = 0
        for i in range(len(s)): 
            sum1+=s[i]*39**i
        s = [y,x][::-1]
        sumYX = 0
        for i in range(len(s)):
            sumYX+=s[i]*39**i
        if sum1%38==0:
            if sumYX**0.5==int(sumYX**0.5):
                print(sumYX)