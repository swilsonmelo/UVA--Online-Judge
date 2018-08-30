from sys import stdin


def main():
    m = list(map(int,stdin.readline().split()))
    while m != []:
        x = m[0]
        y = m[1]
        cont = 0
        r = 0
        while x > 0:
            cont += x
            r += x
            x = r // y
            r = r % y
        print(cont)
        m = list(map(int,stdin.readline().split()))
main()
