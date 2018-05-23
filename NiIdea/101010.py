import sys
def fun():
    n = int(sys.stdin.readline())
    lista = list(map(int,sys.stdin.readline().split()))
    lista1 = []
    for i in range(n):
        if lista[i] not in lista1:
            lista1.append(lista[i])
    
    torres = []
    for i in range(len(lista1)):
        cont = 0
        for j in range(n):
            if lista1[i] == lista[j]:
                
                cont += 1
        torres.append(cont)

    print(max(torres),len(torres))
    
fun()
