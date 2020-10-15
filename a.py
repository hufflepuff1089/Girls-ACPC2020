with open("welcome.in", "r") as f:
    n = int(f.readline().strip())
    for i in range(n):
        a = int(f.readline().strip())
        print(abs(a-2020))