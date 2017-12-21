import sys

def func1():
    n = list(map(int,sys.stdin.readline().split()))
    print(n[0],n[1])
    while n != [0,0]:
        lista = []
        for i in range(n[0]):
            x = int(sys.stdin.readline())
            lista.append(x)
        lista.sort()
        mod = []
        mods = []
        for i in range(-n[1]+1,n[1]):
            mod.append(i)
            mods.append([])
        
        
        for i in range(len(lista)):
            z = abs(lista[i]) % n[1]
            if lista[i]<0:
                z = -z
            mods[mod.index(z)].append(lista[i])
        
        mods1=[]
        for i in range(len(mods)):
            if len(mods[i]) != 0:
                impares = []
                pares = []
                for j in range(len(mods[i])):
                    if mods[i][j] % 2 == 0:
                        pares.append(mods[i][j])
                    else:
                        impares.append(mods[i][j])
                pares.sort()
                impares.sort()
                impares = impares[::-1]
                
                for x in range(len(impares)):
                    mods1.append(impares[x])
                for x in range(len(pares)):
                    mods1.append(pares[x])
        for i in range(len(mods1)):
            print(mods1[i])
        n = list(map(int,sys.stdin.readline().split()))
        print(n[0],n[1])
        
    
func1()
