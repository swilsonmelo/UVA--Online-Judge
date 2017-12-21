from sys import stdin
def main():
    n = int(stdin.readline())
    for i in range(n):
        m = list(map(int,stdin.readline().split()))
        func(m)


def func(m):
    for i in range(1,len(m)):
        if m[i] - 1 != m[i-1]:
            print("N")
            return
    print("Y")
    return





main()
