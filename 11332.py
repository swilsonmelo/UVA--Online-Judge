from sys import stdin

def recu(m):
    if len(m) == 1:
        print(m[0])
    else:
        suma = 0
        for i in range(len(m)):
            suma = suma + int(m[i])

        return recu(str(suma))
def main():
    n = str(stdin.readline().strip())

    while n[0] != "0":
        recu(n)
        n = str(stdin.readline().strip())
main()
