from sys import stdin

def main():
    n = int(stdin.readline())
    for i in range(n):
        m = list(map(int,stdin.readline().split()))
        b = m[0] + m[1]
        p = m[-1]
        func(b,p)

def func(b,p):
    m = [0] * b
    cont = 0
    while len(m)>= p :
        for i in range(p):
            m.pop(0)
        m.append(0)
        cont += 1

    print(cont)
main()
