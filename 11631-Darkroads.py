from sys import stdin

class DisjoinSet(object):
    def __init__(self, n):
        self.padre = [x for x in range(n)]
        self.rank = [0 for x in range(n)]

    def Buscar(self, x):
        if(self.padre[x]!=x):
            self.padre[x]=self.Buscar(self.padre[x])
        return self.padre[x]

    def Union(self, x, y):
        xRaiz = self.Buscar(x)
        yRaiz = self.Buscar(y)
        if(xRaiz == yRaiz):
            return
        if self.rank[xRaiz] < self.rank[yRaiz]:
            self.padre[xRaiz] = yRaiz
        elif self.rank[xRaiz] > self.rank[yRaiz]:
            self.padre[yRaiz] = xRaiz
        else:
            self.padre[yRaiz] = xRaiz
            self.rank[xRaiz]+=1

def kruskal(arcos,m):
    un = DisjoinSet(m)
    cost = 0
    for i in range(len(arcos)):
        if un.Buscar(arcos[i][1]) != un.Buscar(arcos[i][2]):
            cost +=arcos[i][0]
            un.Union(arcos[i][1],arcos[i][2])
    return cost

def main():
    m= list(map(int,stdin.readline().split()))
    while m != [0,0]:
        distancia = []
        suma = 0
        for i in range(m[1]):
            nodos = list(map(int,stdin.readline().split()))
            suma += nodos[2]
            distancia.append([nodos[2],nodos[0],nodos[1]])
        distancia.sort()
        cost = kruskal(distancia,m[0])
        print(suma-cost)
        m = list(map(int,stdin.readline().split()))
main()
