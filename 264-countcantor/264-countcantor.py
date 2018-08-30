from sys import stdin
from math import *

def main():
    n= stdin.readline().strip()
    while n:
        n= int(n)
        k = int(sqrt(2*n)-1)
        while n > ((k*(k+1))/2):
            k += 1
        num = n - ((k*(k-1))/2)
        if k % 2 == 0:
            a = num
            b = k+1-num
        else:
            b = num
            a = k+1-num
        print("TERM",n,"IS", str(int(a))+"/"+str(int(b)))

        n = stdin.readline().strip()
        
main()
