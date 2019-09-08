from sys import stdin
from itertools import *
import math

z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def solve(a,n):
    s = ""
    for i in range(len(a)-1):
        s += a[i]*((n-1))
        for j in range(i+1,len(a)):
            s += (a[i]+a[j])*((n-1))
    s += a[-1]*((n-1))
    return s
"""
def solve(a,r):
    x = ""
    a = product(a, repeat=r)
    matriz = []
    for i in a:
        matriz.append("".join(list(i)))
    x+=matriz[0]
    for i in range(1,len(matriz)):
        print(x,x[-(r-1):],matriz[i][:r-1])
        if x[-(r-1):] == matriz[i][:r-1]:
            x = x[:-(r-1)]+matriz[i]
        else:
            x += matriz[i]
    print(x,len(x),matriz)
"""
def main():
    l = [int(x) for x in stdin.readline().strip().split()]
    
    while l:
        k = l[0]
        n = l[1]
        #s = solve(z[:k],n)
        r = solve(z[:k],n)
        print(r,len(r))
        l = [int(x) for x in stdin.readline().strip().split()]

        

main()
