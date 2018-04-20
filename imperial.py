from sys import stdin


def buscar(x):
    global graph,nodos,padres
    if (padres[x] != x):
        padres[x] = buscar(padres[x])
    return padres[x]

def union(x,y):
    global graph,nodos,padres

##    print(padres)
##    print(cont)
    xraiz = buscar(x) 
    yraiz = buscar(y)
##    print(xraiz,yraiz)
    if(xraiz != yraiz):
        padres[yraiz] = xraiz
        return 1
    return 0
        


def solve():
    global graph,nodos,padres
    vis = [0] * (nodos+1)
    inDegree = [[0,i] for i in range(nodos+1)]
    for i in range(1,nodos+1):
        u = i
        for j in range(len(graph[u])):
            inDegree[u][0] += 1
    inDegree.sort()
    print(inDegree)
    #print(padres)
    for i in range(nodos,0,-1):
        u = inDegree[i][1]
        if vis[u] == 0:
            vis[u] = 1
            for j in range(len(graph[u])):
                v = graph[u][j]
                if vis[v] == 0:
                    union(u,v)
                    vis[v] = 1
    print(padres)
    cont = 1
    for i in range(1,nodos+1):
        u = i
        for j in range(len(graph[u])):
            v = graph[u][j]
            cont += union(u,v)
    print(cont)
            

def main():
    global graph,nodos,padres
    nodos = int(stdin.readline().strip())
    while nodos != -1:
        padres = [i for i in range(nodos+1)]
        graph = [[] for i in range(nodos+1)]
        arcos = [int(x) for x in stdin.readline().strip().split()]
        for i in range(nodos-1):
            u = arcos[i]
            v = i + 2
            #print(u,v)
            graph[u].append(v)
            graph[v].append(u)

        for i in range(nodos+1):
            print(i,graph[i])
            
        solve()
        print()
        
        nodos = int(stdin.readline().strip())
           
    

main()
