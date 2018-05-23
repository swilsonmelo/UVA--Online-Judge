from sys import stdin
from collections import deque


visitados = [-1]*10000
vec = [1,-1]



"""
def grafo(u):
    vecinos = []
    for i in range(4):
        for j in range(2):
            v = u
            v = v[:i]+str((int(v[i])+vec[j])%10)+v[i+1:]
            #print(v)
            vecinos.append(v)
    return vecinos
"""

#grafo("1234")
def bfs(src,target):
    global visitados
    q = deque([])
    q.appendleft(src)
    visitados[int(src)] = 1
    while q:
        u = q.pop()
        #vecinos = grafo(u)
        #print(vecinos)
        for i in range(4):
            v1 = u
            v1 = v1[:i]+str((int(v1[i])+1)%10)+v1[i+1:]
            v2 = u
            v2 = v2[:i]+str((int(v2[i])-1)%10)+v2[i+1:]
            if visitados[int(v1)] == 0:
                #print(v)
                visitados[int(v1)] += 1 + visitados[int(u)]
                if v1 == target:
                    return visitados[int(v1)]-1
                q.appendleft(v1)
            if visitados[int(v2)] == 0:
                #print(v)
                visitados[int(v2)] += 1 + visitados[int(u)]
                if v2 == target:
                    return visitados[int(v2)]-1
                q.appendleft(v2)
                                    
    return -1    
            



def main():
    global visitados
    cases = int(stdin.readline().strip())
    for ca in range(cases):
        visitados = [0]*10000
        start = [str(x) for x in stdin.readline().strip().split()]
        target = [str(x) for x in stdin.readline().strip().split()]
        start =  ("".join(start))
        target = ("".join(target))
        bloqueos = int(stdin.readline().strip())
        for i in range(bloqueos):
           a = [str(x) for x in stdin.readline().strip().split()]
           a = int("".join(a))
           visitados[a] = -1
    

        #print(start,target)
        if start == target or visitados[int(target)] == -1 or visitados[int(start)] ==-1 :
            print(-1)
        else:
            print(bfs(start,target))
        blank = stdin.readline().strip()
        

main()
