from sys import stdin
from math import *


def func(m):
    r = []
    for i in range(1,len(m)-1):
        if m[i] != m[i-1]:
            r.append(abs(m[i] - m[i-1]))
    x = r[0]
    for i in r:
        x = gcd(x,i)
    print(x)
    

def main():
    m = list(map(int,stdin.readline().split()))
    while m[0] != 0:
        func(m)
        m = list(map(int,stdin.readline().split()))
main()
