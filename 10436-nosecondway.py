from sys import stdin

class DisjoinSet(object):
    def __init__(self, n):
        self.padre = [x for x in range(n+1)]
        self.rank = [0 for x in range(n+1)]
 
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
    used=[]
    for i in range(len(arcos)):
        if un.Buscar(arcos[i][1]) != un.Buscar(arcos[i][2]):
            cost +=arcos[i][0]
            un.Union(arcos[i][1],arcos[i][2])
            used.append(arcos[i])
    return used,cost
def main():
    n = int(stdin.readline())
    for i in range(n):
        arcos = []
        m,n = [int(x) for x in stdin.readline().strip().split()]
        vali = 0
        for j in range(n):
            x,y,p = [int(x) for x in stdin.readline().strip().split()]
            if x!=y:
                vali += 1
            arcos.append([p,x,y])
        if vali < m-1:
            print("Case #"+str(i+1)+" : No way")
        else:
           
            r = False
            arcos.sort()
            q=2**31-1
            used,cost1=kruskal(arcos,m)
            if len(used) == m-1:
                for j in used:
                    copia = arcos.copy()
                    del copia[arcos.index(j)]
                    z,r = kruskal(copia,m)
                
                    if r > cost1 and r < q and len(z) == m-1:
                        q = r
                        r = True
                
                if q > cost1 and q != 2**31-1 and r:
                    print("Case #"+str(i+1)+" : "+str(q))
                elif not r :
                    print("Case #"+str(i+1)+" : No way")
                else:
                    print("Case #"+str(i+1)+" : No second way")
            else:
                print("Case #"+str(i+1)+" : No way")

            
main()
            
        
