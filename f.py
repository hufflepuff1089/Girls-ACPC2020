from math import sqrt, pi

f = open('carthage.in')

T = int(f.readline().strip())

for _ in range(T):
    a, l = map(int, f.readline().strip().split())
    
    print(sqrt(a/pi)*2.0*pi/l)
