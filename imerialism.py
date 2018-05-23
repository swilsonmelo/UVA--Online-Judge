from sys import stdin
from collections import deque

def bfs(start):
    global graph,nodos
    profund = [[0,i] for i in range(nodos+1)]
    profund[start][0] += 1
    q = deque([])
    q.appendleft(start)
    while q:
        u = q.pop()
        for i in range(len(graph[u])):
            v = graph[u][i]
            if profund[v][0]== 0:
                q.appendleft(v)
                profund[v][0] = 1 + profund[u][0]
    #print(profund)
    profund.sort()
    
    return profund

def solve():
    global graph,nodos
    profund = bfs(1)
    nodo = profund[-1][1]
    profund = bfs(nodo)
    diametro = profund[-1][0]
    print(diametro//2)




def main():
    global graph,nodos,padres
    nodos = int(stdin.readline().strip())
    while nodos != -1:
        graph = [[] for i in range(nodos+1)]
        arcos = [int(x) for x in stdin.readline().strip().split()]
        for i in range(nodos-1):
            u = arcos[i]
            v = i + 2
            #print(u,v)
            graph[u].append(v)
            graph[v].append(u)

        #for i in range(nodos+1):
        #   print(i,graph[i])

        if nodos == 2:
            print(1)
        else:
            solve()
        #print()
        
        nodos = int(stdin.readline().strip())
           
    

main()
