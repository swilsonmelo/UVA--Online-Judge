from sys import stdin

def main():
    n = stdin.readline().strip()
    while n :
        n = int(n)
        k = int((n+1)/2)
        k *= 2 * k
        print(3*(k-3))
        n = stdin.readline().strip()


main()
