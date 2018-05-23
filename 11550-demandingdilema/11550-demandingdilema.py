from sys import stdin

def func(ma,n,m):
    t = True
    matriz = [[0 for i in range(50)]for j in range(50)]
    for i in range(m):
        cont = 0
        for j in range(n):
            if ma[j][i] == 1:
                if cont == 0:
                    x = j
                else:
                    y = j
                cont += 1
        if cont != 2:
            t = False
        else:
            if matriz[x][y] == 1:
                t = False
            else:
                matriz[x][y] = 1
                matriz[y][x] = 1
    return t

def main():
    c = int(stdin.readline())
    for x in range(c):
        ma = [[0 for i in range(50)]for j in range(50)]
        n,m = [int(y) for y in stdin.readline().split()]
        for i in range(n):
            l = list(stdin.readline().split())
            for j in range(m):
                ma[i][j] = int(l[j])
        t = func(ma,n,m)
        if t:
            print("Yes")
        else:
            print("No")


main()
        
