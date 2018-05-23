from sys import stdin

def main():
    n = int(stdin.readline())
    for i in range(n):
        m = list(map(int,stdin.readline().split()))
        m.sort()
        print("Case "+str(i+1)+":",str(m[1]))
main()
