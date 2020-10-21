f = open('rapunzel.in')

T = int(f.readline().strip())

b_pref = []

def sum_b(start, end):
    global b_pref
    if end < start: return 0
    if start > 0:
        return sum_b(0, end) - sum_b(0, start - 1)
    return b_pref[end]

b_pref = [0 for _ in range(100001)]
for _ in range(T):
    n, k, l = map(int, f.readline().strip().split())
    a = list(map(int, f.readline().strip().split()))
    b = list(map(int, f.readline().strip().split()))

    b_pref[0] = b[0]
    for i in range(1, len(b)):
        b_pref[i] = b_pref[i-1] + b[i]
    
    best = -1
    for i in range(n):
        if best != -1: break

        lo = i
        hi = n

        while abs(hi - lo) > 2:
            mid = (lo + hi) // 2

            x = l * a[i] + sum_b(i+1, mid)

            #print(i, mid, x)

            if x >= k - 1 and x <= k + 1:
                best = i+1
                break
            
            if x > k + 1:
                hi = mid
            elif x < k - 1:
                lo = mid + 1
        
        if best == -1:
            for v in range(lo, hi):
                x = l * a[i] + sum_b(i+1, v)
                if x >= k - 1 and x <= k + 1:
                    best = i+1

    print(best)
