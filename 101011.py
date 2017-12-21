import sys
"""
def busqueda(x,lista1,lista2):
    mid = (len(lista2))//2
    if lista2[mid] == x   :
        return lista1.index(lista2[mid])+1
    elif lista2 [mid] > x and lista2[mid-1] < x :
        return lista1.index(lista2[mid])

    elif lista2 [mid] < x and lista2[mid+1]> x :
        return lista1.index(lista2[mid])+1

    elif lista2[mid] < x:
        return busqueda(x,lista1,lista2[mid:])

    elif lista2[mid] > x:
        return busqueda(x,lista1,lista2[:mid])
"""
def busqueda(x,lista1,lista2):
    mid = (len(lista2))//2
    if lista2[0] > x :
        return lista1.index(lista2[0])
    elif lista2[-1] > x:
        return lista1.index(lista2[-1])
    elif lista2[mid] > x :
        return busqueda(x,lista1,lista2[:mid])
    elif lista2[mid] < x :
        return busqueda(x,lista1,lista2[mid:])

    
def main():
    n1 = int(sys.stdin.readline())
    lista = list(map(int,sys.stdin.readline().split()))
    n2 = int(sys.stdin.readline())
    lista.sort()
    print(lista)
    for i in range(n2):
        x = int(sys.stdin.readline())
        if x >= lista[-1]:
            print(len(lista))
        elif x < lista[0]:
            print(0)
        else:
            y = busqueda(x,lista,lista)
            print(y)
            

main()
