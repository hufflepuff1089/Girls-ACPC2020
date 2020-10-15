f = open('name.in')

def getInt():
    return int(f.readline().strip())

T = getInt()

def near(a, b):
    ctr = 0
    if len(a) != len(b):
        return False
    for x,y in zip(a,b):
        if x != y:
            ctr += 1
    if ctr <= 1: return True
    return False

def connect(G, comp, start, name):
    if comp[start] != -1: return
    comp[start] = name
    for v in G[start]:
        connect(G, comp, v, name)


for _ in range(T):
    N, K = map(int, f.readline().strip().split())
    G = {}
    component = {}
    
    for i in range(N):
        name = f.readline().strip()
        G[name] = set()
        component[name] = -1
    
    for a in G.keys():
        for b in G.keys():
            if a != b and near(a, b):
                G[a].add(b)
                G[b].add(a)
    
    for i,a in enumerate(G.keys()):
        connect(G, component, a, i)
    
    for j in range(K):
        a, b = f.readline().strip().split()
        if a in G and b in G and component[a] == component[b] and component[a] != -1:
            print("Yes")
        else:
            print("No")


