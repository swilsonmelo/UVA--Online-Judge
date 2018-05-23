from sys import stdin
from collections import deque


vecinos = [[1,0,0,0],[-1,0,0,0],[0,1,0,0],[0,-1,0,0],[0,0,1,0],[0,0,-1,0],[0,0,0,1],[0,0,0,-1]]


def grafo(v1,k):
    global visit,dist,visitmat

    v2 = []
    for i in range(4):
        v1[i] = (v1[i] + vecinos[k][i])%10
        if visitmat[i][v1[i]] == 1:
            #print("kha")
            return v1,False
        v2.append(str(v1[i]))
    return v1,v2

def bfs(src,target):
    global visit,dist,visitmat
    
    q = deque([])
    q.appendleft(src)
    while q:
        u = q.pop()
        ucop = []
        for i in range(4):
            ucop.append(str(u[i]))
        for i in range(8):
            v = u.copy()
            v,vcop = grafo(v,i)
            if vcop == False:
                #print(v)
                continue   
            if (not " ".join(vcop) in visit) :
                visit[" ".join(vcop)] = True
                dist[" ".join(vcop)] =  dist[" ".join(ucop)] + 1
                if v == target:
                    #print("kah")
                    return dist[" ".join(vcop)]
                
                q.appendleft(v)
                
    return -1    
            



def main():
    global visit,dist,visitmat
    cases = int(stdin.readline().strip())
    for ca in range(cases):
        visit = {}
        dist = {}
        visitmat = [[0]*10]*(4)
        src = [ int(x) for x in stdin.readline().strip().split()]
        target = [ int(x) for x in stdin.readline().strip().split() ]
        ini = []
        for i in range(4):
            ini.append(str(src[i]))
        dist[" ".join(ini)] = 0
        visit[" ".join(ini)] = True
        bloqueos = int(stdin.readline().strip())
        for i in range(bloqueos):
            a = [str(x) for x in stdin.readline().strip().split()]
            if a != ini:
                for j in range(4):
                    visitmat[j][int(a[j])] = 1
            visit[" ".join(a)] = True

        for i in visitmat:
            print(i)

        
        if src == target:
            print(0)
        else:
            print(bfs(src,target))
        if ca < cases-1:
            a = stdin.readline()

main()
