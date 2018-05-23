from sys import stdin

def main():
    n = int(stdin.readline())
    for i in range(n):
        m = list(map(int,stdin.readline().split()))
        print("Case",str(i+1)+":",max(m[1:]))

main()
