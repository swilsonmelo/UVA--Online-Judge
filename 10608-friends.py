from sys import stdin

class DisjoinSet(object):
    def __init__(self, n):
        self.padre = [x for x in range(n)]
        self.rank = [0 for x in range(n)]
        self.tam = [1 for x in range(n)]

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
            tmp = self.tam[yRaiz]
            self.tam[yRaiz] += self.tam[xRaiz]
            self.tam[xRaiz] += tmp
        elif self.rank[xRaiz] > self.rank[yRaiz]:
            self.padre[yRaiz] = xRaiz
            tmp = self.tam[xRaiz]
            self.tam[xRaiz] +=  self.tam[yRaiz]
            self.tam[yRaiz] += tmp
            
        else:
            self.padre[yRaiz] = xRaiz
            tmp = self.tam[xRaiz]
            self.tam[xRaiz] += self.tam[yRaiz]
            self.tam[yRaiz] += tmp
            self.rank[xRaiz]+=1

def main():
    n = int(stdin.readline())
    for i in range(n):
        z = list(map(int,stdin.readline().split()))
        nodos = z[0]
        m = z[1]
        y = DisjoinSet(nodos)
        for j in range(m):
            z = list(map(int,stdin.readline().split()))
            p1 = z[0]-1
            p2 = z[1] -1
            if y.Buscar(p1) != y.Buscar(p2):
                y.Union(p1,p2)
        print(max(y.tam))


main()
            
        
