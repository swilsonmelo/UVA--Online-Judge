from sys import stdin

def main():
    n = int(stdin.readline())
    for i in range(n):
        x = int(stdin.readline())
        z = ((((x*567)/9) + 7492) * 235 /47)  - 498
        z = str(int(z))
        print(z[-2])
main()
