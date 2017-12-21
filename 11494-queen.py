from sys import stdin

a, b, c, d = list(map(int,stdin.readline().split()))
while True:
    if not any([a, b, c, d]):
        break
    if (a, b) == (c, d):
        print (0)
    elif a == c or b == d or a + b == c + d or abs(a - c) == abs(b - d):
        print (1)
    else:
        print (2)
    a, b, c, d = list(map(int,stdin.readline().split()))
