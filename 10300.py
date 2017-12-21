
from sys import stdin


def opera(m):
    tam = m[0]
    cant = m[1]
    espa = tam/cant
    z = espa*m[2]
    x = z*cant
    return x

def main():
    n = int(stdin.readline())
    for  i in range(n):
        g = int(stdin.readline())
        suma = 0
        for j in range(g):
            m = list(map(int,stdin.readline().split()))
            suma = suma + opera(m)
        print(int(suma))


main()
