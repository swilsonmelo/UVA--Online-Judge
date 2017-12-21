from sys import stdin

def main():
    n = stdin.readline().split()
    while n:
        n = int(n[0])*2
        x = int((n)**0.5)
        if x*(x+1) < n:
            x += 1
        n = int(n/2)
        r = int(n - x *(x-1)/2)
        print(str((x-r+1))+"/"+str(r))
        n = stdin.readline().split()

main()
