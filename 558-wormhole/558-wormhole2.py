from sys import stdin



def bellmanFord(ini,fin,cost,distancia,nodos,arcos):

    for i in range(nodos):
        for j in range(arcos):
            u = ini[j]
            v = fin[j]
            costo = cost[j]
            if(distancia[v] > distancia[u] + costo):
                distancia[v] = distancia[u] + costo
    """
    for i in range(arcos):
        print(distancia[i])
    for i in range(arcos):
        u = ini[i]
        v = fin[i]
        costo = cost[i]
        print(distancia[u],distancia[v],costo)
    """
    for i in range(arcos):
        u = ini[i]
        v = fin[i]
        costo = cost[i]
        print(distancia[u],distancia[v],costo , distancia[v] > (distancia[u] + costo) )
        if distancia[v] > distancia[u]:
            r = 1
        else:
            r = 0
        if r + costo > 0:
            return True
        
        else:
            return False

def main():
    cases = int(stdin.readline().strip())
    for ca in range(cases):
        nodos,arcos = [ int(x) for x in stdin.readline().strip().split() ]
        distancia = [ 10000000000 for x in range(nodos+1)]
        ini = [0]*arcos
        fin = [0]*arcos
        cost = [0]*arcos
        for i in range(arcos):
            u,v,d = [int(x) for x  in stdin.readline().strip().split()]
            ini[i] = u
            fin[i] = v
            cost[i] = d

        r = bellmanFord(ini,fin,cost,distancia,nodos,arcos)
        if r == True:
            print("possible")
        else:
            print("not possible")
        

main()
