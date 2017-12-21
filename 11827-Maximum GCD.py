from sys import stdin
from math import *

def func(m):
    maxi = 0
    for i in range(len(m)-1):
        for j in range(i+1,len(m)):
            maxi = max(maxi,gcd(m[i],m[j]))
    print(maxi)
def main():
    n = int(stdin.readline())
    for i in range(n):
        m = list(map(int,stdin.readline().split()))
        func(m)
main()
    
