def f(n,a):
    s = ''
    while n > 0:
        s = str(n%a) + s
        n //= a 
    return s
value = 2*729**333 + 2*243**334 - 81**335 + 2*27**336 - 2*9**337 - 338
answer = f(value,9)
print(len(answer) - answer.count('0'))
