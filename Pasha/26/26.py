with open("Pasha/26_2024.txt") as f:
    N = int(f.readline()[:-1])
    timing = []
    for i in range(N):
        x, y = map(int, f.readline().split())
        timing.append((x, y))
    timing.sort()
    pass
