from sys import stdin
from collections import deque


def main():
    conta = 1
    global dic
    global G
    n  = list(stdin.readline().split())
    while  n != []:
        dic = {}
        G = []
        for i in range(int(n[0])):
            y = stdin.readline().strip()
            G.append([y,[]])
            dic[y] = i
        n2 = int(stdin.readline())
        for j in range(n2):
            m = list(stdin.readline().split())
            G[dic[m[0]]][1] += [m[1]]
        blank = stdin.readline()
        print(kahn_topsort(dic))
        #print("Case #"+str(conta)+": Dilbert should drink beverages in this order:"," ".join(list(topoSort(dic)))+".")
        n  = list(stdin.readline().split())
        conta+=1



def kahn_topsort(graph):
    in_degree ={ u[0] : 0 for u in G }
    for u in range(len(G)):
        for v in G[u][1]:
            in_degree[v] += 1
    Q,L= deque(),[]
    for u in in_degree:
        if in_degree[u] == 0:
            Q.appendleft(u)
    while Q:                
        u = Q.pop()
        L.append(u) 
        for v in range(len(G)):
            in_degree[G[v][0]] -= 1
            if in_degree[G[v][0]] == 0:
                print(G[v][0])
                Q.appendleft(G[v][0])
 
    if len(L) == len(G): return L
    else:  return []
main()
