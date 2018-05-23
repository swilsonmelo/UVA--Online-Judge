from sys import stdin
from math import *

def factores(n):
    fac = set()
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            fac.add(i)
            fac.add(n//i)
    fac = list(fac)
    fac.sort()
    return fac

def main():
    n = int(stdin.readline())
    while n != 0:
        cont = 0
        fac = factores(n)
        for i in range(len(fac)-1):
            for j in range(i,len(fac)):
                if int((fac[i]*fac[j])/gcd(fac[i],fac[j])) == n:
                    cont += 1
        print(n,cont+1)   
        n = int(stdin.readline())
    

    
main()
