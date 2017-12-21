from sys import stdin

def sinvisitar(x,vis,salida,graph):
    
    for i in x:
        if vis[i] == False:
            vis[i] = True
            salida.add(i)
            vis,salida = sinvisitar(graph[i],vis,salida,graph)
    return vis,salida


def main():
    n = int(stdin.readline())
    while n != 0:
        graph = {}
        tnodos = set()
        for i in range(n):
            graph[i+1] = []
            tnodos.add(i+1)
        m = list(map(int,stdin.readline().split()))
        while m != [0]:
            graph[m[0]] += m[1:-1]
            m = list(map(int,stdin.readline().split()))
        nodos = list(map(int,stdin.readline().split()))
        for i in nodos[1:]:
            salida= set()
            vis= [False]*(n+1)
            vis,salida = sinvisitar(graph[i],vis,salida,graph)
            x = list(tnodos - salida)
            x.sort()
            x = list(map(str,x))
            if len(x) > 0:
                print(len(x)," ".join(x))
            else:
                print(0)
            

        n = int(stdin.readline())
            
main()
