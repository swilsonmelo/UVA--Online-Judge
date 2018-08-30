from sys import stdin
m1 = stdin.readline().strip().split()
while m1:
    m2 = stdin.readline().strip().split()
    m1 = set(m1)
    m2 = set(m2)
    x = len(m1)
    y = len(m2)
    if m1 == m2:
        print("A equals B")
    elif x > y and len(m2-m1) == 0:
        print("B is a proper subset of A")
    elif x < y and len(m1-m2) == 0:
        print("A is a proper subset of B")
    elif m1 != m2:
        if len(m1 & m2) != 0:
            print("I'm confused!")
        else:
            print("A and B are disjoint")
    m1 = stdin.readline().strip().split()
    
 
