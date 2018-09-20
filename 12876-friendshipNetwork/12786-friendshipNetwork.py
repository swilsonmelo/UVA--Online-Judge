from sys import stdin
from heapq import *

def main():
    m = [int(x) for x in stdin.readline().strip().split()]
    while m:
        heap = []
        heapify(heap)
        n = m[0]
        for i in range(n):
            heappush(heap,-m[1+i])
        isCorrect = True
        #print(heap)
        while heap:
            sig = heappop(heap)
            #print("Sig",sig)
            if len(heap) < abs(sig):
                isCorrect = False
                break
            edges = []
        
            for i in range(abs(sig)):
                xi = heappop(heap)
                #print(xi)
                edges.append(xi +1 )

            #print(edges,sig)
            for i in range(abs(sig)):
                if edges[i] != 0:
                    heappush(heap,edges[i])

        if isCorrect:
            print(1)
        else:
            print(0)
        #print(heap)
        m = [int(x) for x in stdin.readline().strip().split()]

main()
