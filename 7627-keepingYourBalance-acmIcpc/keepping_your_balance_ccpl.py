from sys import stdin
import math

def salida(x,y):
    z = int(x*(x-1)/math.gcd(x,(x-1)))
    for i in range(x-y-1):
        x = x-1
        z = int(z)
        z = z*(x-1)/math.gcd(z,(x-1))

    print(z)
    
    

def main():
    m = list(map(int,stdin.readline().split()))
    while m[0] != -1:
        salida(m[0],m[1])
        m = list(map(int,stdin.readline().split()))
        
main()
