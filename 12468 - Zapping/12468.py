from sys import stdin

def main():
    m = list(map(int,stdin.readline().split()))
    top = 99
    while m != [-1,-1]:
        x = min(m[0],m[1])
        y = max(m[0],m[1])
        if abs(x-y) < abs((x+100) - y):
            print(abs(x-y))
        else:
            print(abs((x+100) - y))
        
        m = list(map(int,stdin.readline().split()))
        
main()
