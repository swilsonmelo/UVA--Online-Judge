import sys
def func():
    n = int(sys.stdin.readline())
    lista1 = list(map(int,sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    lista2 = list(map(int,sys.stdin.readline().split()))

    
    for i in range(m):
        y = True
        while y :
            if lista2[i] <= lista1[0]:
            
                y = False
                print(1)
            elif lista2[i] >= sum(lista1[:-1]):
                
                y = False
                print(len(lista1))
            else:
                for j in range(0,n):
                    if lista2[i]<=sum(lista1[:j]):
                        
                        print(j)
                        y = False
                        break
                    
            if not y :
                break
    
func()
