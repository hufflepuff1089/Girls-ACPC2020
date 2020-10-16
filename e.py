from math import sqrt

f = open('smart.in')
T = int(f.readline().strip())

def value(x, y, a, b, c):
    h = sqrt((x - c)**2 + y**2)
    k = sqrt((a - c)**2 + b**2)
    t = h/2.0 + k
    return t

for _ in range(T):
    x, y = map(float, f.readline().strip().split())
    a, b = map(float, f.readline().strip().split())

    lo = min(x, a)
    hi = max(x, a)

    t = 0

    while(abs(hi - lo) > 0.001):

        p1 = lo + (hi - lo) / 3
        p2 = hi - (hi - lo) / 3

        v1 = value(x, y, a, b, p1)
        v2 = value(x, y, a, b, p2)

        if v1 > v2:
            lo = p1
        else:
            hi = p2


    print(value(x, y, a, b, (lo + hi) / 2))
