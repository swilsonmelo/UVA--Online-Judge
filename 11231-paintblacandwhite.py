from sys import stdin

m = stdin.readline().strip().split()
while m != ["0","0","0"]:
    p,n,c = [int(x) for x in m]
    p -= 7
    n -= 7
    if (p % 2 and n % 2) and c:
        print(p * n // 2 + 1)
    else:
        print(p*n // 2)
    m = stdin.readline().strip().split()
