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


def distancia(x,y):
    d =(((x[0]-y[0])**2)+((x[1]-y[1])**2))**(1/2)
    R = max(x[2],y[2])
    r = min(x[2],y[2])
    if R > d :
        if d+r > R:
            return True
        else:
            return False
    else:
        if d > R+r:
            return False
        else:
            return True

def main():
    global union
    n = int(stdin.readline())
    while n != -1:
        union = {}
        m = DisjoinSet(n)
        rings = []
        for i in range(n):
            union[i] = i
            rings.append(list(map(float,stdin.readline().split()))+[i])
        for i in range (len(rings)):
            for j in range(i+1,len(rings)):
                if distancia(rings[i],rings[j]):
                    if m.Buscar(union[rings[i][3]]) !=  m.Buscar(union[rings[j][3]]):
                        m.Union(union[rings[i][3]],union[rings[j][3]])
        y = max(m.tam)
        if y == 1:
            print("The largest component contains 1 ring.")   
        else:
            print("The largest component contains",y,"rings.")
            
        n = int(stdin.readline())
main()            
