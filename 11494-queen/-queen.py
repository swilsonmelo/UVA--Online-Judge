from sys import stdin
def main():
    a, b, c, d = list(map(int,stdin.readline().split()))
    while a !=0 and b !=0 and c != 0 and d !=0:
        if not any([a, b, c, d]):
            break
        if (a, b) == (c, d):
            print (0)
        elif a == c or b == d or a + b == c + d  or abs(a - c) == abs(b - d):
            print (1)
        else:
            print (2)
        a, b, c, d = list(map(int,stdin.readline().split()))
main()
