
def to_Triple(n,system):
    tr = ""
    while n > 0:
        tr = str(n%system) + tr
        n //= system
    return tr

