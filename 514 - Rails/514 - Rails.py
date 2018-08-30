from sys import stdin
def func(n,lista,l):
    cola = []
    l = list(set(range(1,n+1)))
    
    if lista == l :
        print("Yes")
    elif lista == l[::-1]:
        print("Yes")
    else:
        cola.append(l.pop(0))
        while len(l) != 0  :
            
            if cola[-1] == lista[0]:
                cola.pop()
                lista.pop(0)
                
                if len(cola) == 0 and len(l) != 0:
                    cola.append(l.pop(0))
                    
                while len(cola) != 0:
                    if cola[-1] == lista[0]:
                        
                        cola.pop()
                        lista.pop(0)
                       
                    else:
                        break
            if len(l) != 0:
                cola.append(l.pop(0))
               
    
        if len(cola) == 0:
            print("Yes")
        else:

            
            if lista == cola[::-1]:
                print("Yes")
            else:
                print("No")
            
    



    
def main():
    n=int(stdin.readline())
    while n!=0:
        listaIn=list(set(range(1,n+1)))
        listaSal=[int(x) for x in stdin.readline().strip().split()]
        while listaSal[0]!=0:
            func(n,listaSal,listaIn)
            listaSal=[int(x) for x in stdin.readline().strip().split()]
        print()
        n=int(stdin.readline())
        
        
        
    
main()
