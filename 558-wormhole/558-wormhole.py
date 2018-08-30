from sys import stdin



def initialize(graph, source):
    d = {} # Stands for destination
    p = {} # Stands for predecessor
    for node in graph:
        d[node] = float('Inf') # We start admiting that the rest of nodes are very very far
        p[node] = None
    d[source] = 0 # For the source we know how to reach
    return d, p

def relax(node, neighbour, pe, graph, d, p):
    # If the distance between the node and the neighbour is lower than the one I have now
    if d[neighbour] > d[node] + pe:
        # Record this lower distance
        d[neighbour]  = d[node] + pe
        p[neighbour] = node

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1): #Run this until is converges
        for u in graph:
            for x in graph[u]: #For each neighbour of u
                v,pe = x[0],x[1]
                relax(u, v, pe, graph, d, p) #Lets relax it

    # Step 3: check for negative-weight cycles
    for u in graph:
        for x in graph[u]:
            v,pe = x[0],x[1]
            if d[v] > d[u] + pe:
                return True

    return False

def main():
    c = int(stdin.readline())
    for i in range(c):
        n,m = [int(x) for x in stdin.readline().strip().split()]
        dic = {x:[] for x in range(n)}
        for j in range(m):
            x1,x2,p = [int(x) for x in stdin.readline().strip().split()]
            dic[x1].append([x2,p])
        d = bellman_ford(dic,0)
        if d:
            print("possible")
        else:
            print("not possible")
main()
        
    
