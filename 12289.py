from sys import stdin

def main():
    uno = { "o" , "n" ,"e" }
    dos = {"t","w","0"}
    n = int(stdin.readline())
    for i in range(n):
        m = list(map(str,stdin.readline().strip()))
        if len(m) == 5 :
            print(3)
        elif len(set(m) & uno) > len(set(m) & dos)  :
            print(1)
        else:
            print(2)

main()
        
