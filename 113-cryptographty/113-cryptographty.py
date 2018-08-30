from sys import stdin

def main():
    n = stdin.readline().strip()
    while n :
        n2 = stdin.readline().strip()
        print(round(int(n2)**(1/int(n))))
        n = stdin.readline().strip()
main()
