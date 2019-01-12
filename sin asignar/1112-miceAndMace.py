from sys import stdin
from heapq import *


def dijkstra(graph,n,src,T):
    pq = []
    heapify(pq)
    dist = [float('inf') for x in range(n+1) ]
    heappush(pq,[src,0])
    dist[src] = 0
    while pq:
        top = heappop(pq)
        u = top[0]
        cost = top[1]
        if (dist[u] == cost and dist[u] <= T):
            for i in range(len(graph[u])):
                v = graph[u][i][0]
                t = graph[u][i][1]
                #print(t,graph[u])
                if( dist[u] + t < dist[v] ):
                    dist[v] = dist[u] + t
                    heappush(pq,[ v,dist[v] ])
    mices = 0
    for i in range(1,n+1):
        if dist[i] <= T:
            mices += 1
    return mices
                


def main():
    cases = int(stdin.readline().strip())
    for ca in range(cases):
        blank = stdin.readline()
        n = int(stdin.readline().strip())
        e = int(stdin.readline().strip())
        t = int(stdin.readline().strip())
        arcos = int(stdin.readline().strip())
        graph = [[] for x in range(n+1)]
        for i in range(arcos):
            u,v,d = [int(x) for x in stdin.readline().strip().split()]
            graph[v].append([u,d])
        r = dijkstra(graph,n,e,t)
        print(r)
        if ca < cases-1:
            print()
main()
