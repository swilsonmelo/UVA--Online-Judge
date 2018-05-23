from sys import stdin

def main():
    n = int(stdin.readline())
    conta = 1
    while n != 0:
        m = list(map(int,stdin.readline().split()))
        suma = 0
        for i in range(n):
            if m[i] > 0 :
                suma += 1
            else:
                suma -= 1
        print("Case",str(conta)+":",suma)
        conta += 1
        n = int(stdin.readline())
main()
