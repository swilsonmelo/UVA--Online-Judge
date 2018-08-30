from sys import stdin


    

def main():
    n = int(stdin.readline())
    conta = 1
    while n != 0:
        m = list(map(int,stdin.readline().split()))
        x = sum(m)
        m.sort()
        valor = x//n
        cont = 0
        while m[0] != valor:
            y = valor - m[0]
            if m[-1] - y < valor :
                y = m[-1] - valor
            m[-1] = m[-1] - y
            m[0] = m[0] + y
            m.sort()
        
            cont = cont + y
        print("Set #"+str(conta))
        print("The minimum number of moves is",str(cont)+".")

        n = int(stdin.readline())
        
        print()        
        conta += 1
        
main()
