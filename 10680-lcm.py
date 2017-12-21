from sys import stdin
import math
top = 100#1000000
m = [0]*top
m[1] = 1
for i in range(2,top):
    x = m[i-1]*i//math.gcd(m[i-1],i)
    x = int(str(x)[::-1])
    x = int(str(x)[::-1])
    m[i] = x


for i in range(1,100):
    print(str(m[i])[-1])

