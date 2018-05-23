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
    cost = 2**31-1
    for i in range(len(arcos)):
        if un.Buscar(arcos[i][1]) != un.Buscar(arcos[i][2]):
            cost =min(cost,arcos[i][0])
            un.Union(arcos[i][1],arcos[i][2])
    
    return cost

def main():
    n = int(stdin.readline())
    for i in range(n):
        arcos = []
        m,r = [int(x) for x in stdin.readline().strip().split()]
        for j in range(r):
            x,y,p = [int(x) for x in stdin.readline().strip().split()]
            arcos.append([p,x,y])
        arcos.sort()
        arcos = arcos[::-1]
        mincost = kruskal(arcos,m)
        print("Case #"+str(i+1)+":",mincost)
        
main()


            
