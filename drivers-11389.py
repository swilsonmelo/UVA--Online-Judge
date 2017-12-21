from sys import stdin
def main():
    m =  list(map(int,stdin.readline().split()))
    
    while m != [0,0,0]:
        dia = list(map(int,stdin.readline().split()))
        noche = list(map(int,stdin.readline().split()))
        h = m[1]
        p = m[-1]
        dia.sort()
        noche.sort()
        func(dia,noche,h,p)
        m = list(map(int,stdin.readline().split()))

def func(dia,noche,h,p):
    cont = 0
    while len(dia) != 0:
        e = dia.pop(0) + noche.pop(-1) - h
        if e > 0:
            cont = cont + e

    print(cont*p)

main()
