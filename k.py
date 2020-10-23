f = open('gracehopper.in')

N, M = map(int, f.readline().strip().split())

cmd = {}
memo = {}
moves = {}

def calc(target):
    global cmd
    global memo
    global moves

    if len(target) == 0: return 0
    if target in memo: return memo[target]
    
    best = None
    bestval = None

    for i in range(1, 11):
        if len(target) < i: break

        if target[:i] in cmd:
            t = calc(target[i:])
            if t != -1:
                if best is None or best > t:
                    best = t
                    bestval = target[:i]
    
    if best is None:
        memo[target] = -1
        return -1
    else:
        memo[target] = best + 1
        moves[target] = bestval
        return best + 1

for _ in range(N):
    op, name = f.readline().strip().split()
    cmd[op] = name

for _ in range(M):
    moves.clear()
    memo.clear()
    target = f.readline().strip()

    res = calc(target)
    print(res)

    if res >= 0:
        while len(target) > 0:
            print(cmd[moves[target]])
            target = target[len(moves[target]):]
