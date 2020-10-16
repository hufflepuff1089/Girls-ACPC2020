with open("computer.in", "r") as f:
    t = int(f.readline().strip())
    for i in range(t):
        n = f.readline().strip()
        uni = n.count('1')
        if uni == 0: print(1)
        else: print(1/2**uni)