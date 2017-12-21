from sys import stdin
from collections import deque
import heapq


n = list(map(int,stdin.readline().split()))
while n != []:
    stack = []
    queue = deque()
    heap = []
    Stack = Queue = Heap = True
    for i in range(n[0]):
        m = list(map(int,stdin.readline().split()))
        if m[0] == 1:
            stack.append(m[1])
            queue.append(m[1])
            heapq.heappush(heap, -m[1])
        elif len(stack)!= 0 or len(queue) != 0 or len(heap) != 0:
            a = stack.pop()
            if a != m[1]:
                Stack = False
            a = queue.popleft()
            if a != m[1]:
                Queue = False
            a = heapq.heappop(heap)
            if a != -m[1]:
                Heap = False
        else:
            Stack = False
            Queue = False
            Heap = False
    l = []
    if Stack:
        l.append(1)
    else:
        l.append(0)
    if Queue:
        l.append(1)
    else:
        l.append(0)
    if Heap:
        l.append(1)
    else:
        l.append(0)
    
    s = sum(l)
    if s >= 2:
        print ('not sure')
    elif s == 0:
        print ('impossible')
    else:
        if Stack:
            print ('stack')
        if Queue:
            print ('queue')
        if Heap:
            print ('priority queue')
    n = list(map(int,stdin.readline().split()))
