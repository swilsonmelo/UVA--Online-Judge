from sys import stdin

def main():
    m = list(map(int,stdin.readline().split()))
    while m != [] :
        r = abs(m[0]-m[1])
        print(r)
        m = list(map(int,stdin.readline().split()))

main()

        
