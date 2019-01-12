from sys import stdin

seive = [True] * 52
seive[0] = seive[1] = False
for i in range(2,51):
    if seive[i] == True:
        for j in range(i*i,51,i):
            seive[j] = False

#print(seive)
def recu(pos,lista,vis,n):
    global salida
    #print(lista,pos)
    
    if pos == n:
        num = lista[-1] + 1
        if seive[num]:
            print(*lista)
        return

    for i in range(2,n+1):
        if  vis[i] == False:
            num = i + lista[-1]
            if seive[num]:
                vis[i] = True
                #print(lista,i)
                lista2 = lista.copy()
                lista2.append(i)
                recu(pos+1,lista2,vis,n)
                vis[i] = False
            


def main():
    global salida
    n = stdin.readline().strip()
    case = 1
    while n :
        n = int(n)
        visitados = [False] * (n+2)
        salida = []
        lista = [1]
        print("Case "+str(case)+":")
        recu(1,lista,visitados,n)
        # print(salida,"alv")
        n = stdin.readline().strip()
        if n:
            print()
        case += 1
main()
