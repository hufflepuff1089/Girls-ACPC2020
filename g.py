import math

def alg(m, h):
    d = math.gcd(m, h)
    m = m // d
    h = h // d
    return m+h

MAXH = 1000

with open("cat.in", "r") as f:
    t = int(f.readline().strip())
    for _ in range(t):
        
        nc, m = map(int, f.readline().strip().split())

        tab = [[-1 for _ in range(MAXH+1)] for _ in range(nc+1)]

        tab[0][m] = 0

        for i in range(0, nc):
            h, e = map(int, f.readline().strip().split(' '))

            for j in range(MAXH):
                tab[i+1][j] = tab[i][j]
                if tab[i][j] == -1:
                    continue

                newh = alg(j, h)
                if newh >= MAXH:
                    continue

                if tab[i+1][newh] == -1 or tab[i+1][newh] > tab[i][j] + e:
                    tab[i+1][newh] = tab[i][j] + e
        """
        for x in tab:
            for y in x:
                print(y, end=' ')
            print()
        """

        res = -1
        for v in tab[-1][0:3]:
            if v != -1:
                if res == -1: res = v
                else: res = min(res, v)
        print(res)
