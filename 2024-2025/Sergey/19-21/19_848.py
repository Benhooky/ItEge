def f(first,turn):
    if first>=51:
        if turn==2:
            return True
        else:
            return False
    if turn>4:
        return False