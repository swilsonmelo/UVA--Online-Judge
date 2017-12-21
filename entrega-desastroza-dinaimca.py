from sys import stdin
lista = [1,1,5]
for i in range(3,42):
    lista.append(lista[i-1]+4*lista[i-2]+2*lista[i-3])


def main():
    n = int(stdin.readline())
    for i in range(n):
        x = int(stdin.readline())
        print(lista[x])
main()
