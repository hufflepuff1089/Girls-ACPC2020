def check(s, d):
    for w in s:
        if w not in d:
            print("Oops")
            return
    for w in s:
        if d[w] > 1:
            print("Confusing")
            return
    print("Unique")
    return





with open("joan.in", "r") as f:
    t = int(f.readline().strip())
    for q in range(t):
        d = {}
        l = int(f.readline().strip())
        for i in range(l):
            word = f.readline().strip()
            w = word[0]
            if w not in d: d[w] = 1
            else: d[w] += 1
        nabb = int(f.readline().strip())
        for i in range(nabb):
            word = f.readline().strip()
            check(word, d)