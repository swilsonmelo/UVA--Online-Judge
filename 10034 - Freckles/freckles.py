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
    un = DisjoinSet(len(m))
    cost = 0
    for i in range(len(arcos)):
        if un.Buscar(arcos[i][1]) != un.Buscar(arcos[i][2]):
            cost +=arcos[i][0]
            un.Union(arcos[i][1],arcos[i][2])
    print("%.2f"%cost)

def distancia(m):
    arcos = []
    for i in range(len(m)-1):
        x1 = m[i][0]
        y1 = m[i][1]
        for j in range(i+1,len(m)):
            x2 = m[j][0]
            y2 = m[j][1]
            distancia = (((y2-y1)**2) + ((x2-x1)**2))**(1/2)
            arcos.append([distancia,i,j])
    return arcos
            

def main():
    casos = int(stdin.readline())
    for i in range(casos):
        v = stdin.readline()
        nodos = stdin.readline()
        m = []
        for j in range(int(nodos)):
            m.append(list(map(float,stdin.readline().split())))
        arcos = distancia(m)
        arcos.sort()
        kruskal(arcos,m)
        if i != (casos-1):
            print()

main()
            
    
