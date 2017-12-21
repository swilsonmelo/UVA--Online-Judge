from sys import stdin

def main():
    n = int(stdin.readline())
    for i in range(n):
        x,y = list(map(int,stdin.readline().split()))
        if x < y:
            print("<")
        elif x > y :
            print(">")
        else:
            print("=")

main()
