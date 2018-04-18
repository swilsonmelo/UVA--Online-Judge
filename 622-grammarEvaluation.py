from sys import stdin


def main():
    cases = int(stdin.readline().strip())
    for i in range(cases):
        a = stdin.readline().strip()
        try:
            print(eval(a))
        except:
            print("ERROR")

main()
