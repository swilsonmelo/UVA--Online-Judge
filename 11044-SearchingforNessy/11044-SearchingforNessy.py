from sys import stdin

def main():
    n= int(stdin.readline())
    for i in range(n):
        m = list(map(int,stdin.readline().split()))
        x = m[0] //3
        y = m[1] //3
        print(x*y)

main()
