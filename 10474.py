
import sys
def main():
    entrada = list(map(int,sys.stdin.readline().split()))
    cont = 1
    while entrada != [0,0] :
        tab = []
        jug = [] 
        for i in range(entrada[0]):
            n = int(sys.stdin.readline())
            tab.append(n)
        for i in range(entrada[1]):
            n = int(sys.stdin.readline())
            jug.append(n)
        tab.sort()
        print("CASE# "+str(cont)+":")
        for i in range(len(jug)):
            if jug[i] in tab:
                
                print(jug[i],"found at",tab.index(jug[i])+1)
            else:
               
                print(jug[i],"not found")
                
        cont +=1
        entrada = list(map(int,sys.stdin.readline().split()))
main()
