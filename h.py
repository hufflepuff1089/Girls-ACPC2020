f = open('masks.in')

T = int(f.readline().strip())

for _ in range(T):
    N = int(f.readline().strip())
    vals = list(map(int, f.readline().strip().split()))
    M = int(f.readline().strip())
    
    res = 0
    while M > 0:
        pos = vals.index(min(vals))
        res += vals[pos]
        vals[pos] += 1
        M -= 1
    print(res)
