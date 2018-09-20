from sys import stdin

def main():
    n = int(stdin.readline().strip())
    while n != 0:
        pesos = [0]*(n+1)
        #graph = [[] for i in range(n+1)]
        padres = [0 for i in range(n+1)]
        deGree = [-1]*(n+1)
        for i in range(n):
            m = [int(x) for x in stdin.readline().strip().split()]
            u = m[0]
            pesos[u] = m[1]
            deGree[u] = m[2]
            for j in range(m[2]):
                
                v = m[3+j]
                
                padres[v] = u

        #print(padres)
        #print(deGree)
        stack = []
        for i in range(1,n+1):
            if deGree[i] == 0:
                stack.append(i)
        costo = 0
        while stack:
            u = stack.pop()
            padre = padres[u]
            deGree[padre] -= 1
            sobra = pesos[u] - 1
            costo += abs(sobra)
            pesos[u] = 1
            pesos[padre] += sobra
            #print(u,padre,sobra,costo)
            if deGree[padre] == 0:
            
                stack.append(padre)
        print(costo)
        #print(stack)
        n = int(stdin.readline().strip())


main()
