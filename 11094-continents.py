from sys import stdin
def imprimir(m):
    for i in range(len(m)):
        print(m[i])


def revisar(m,i,j,key,cont,conta):
    if j == len(m[i])-2:
        if m[i][1] == key :
            m[i][1] = cont
            conta += 1
            m,conta = revisar(m,i,1,key,cont,conta)
    if j == 1:
    
        if m[i][len(m[i])-2] == key :
            m[i][len(m[i])-2] = cont
            conta += 1
            m,conta = revisar(m,i,len(m[i])-2,key,cont,conta)
            
            
     
    if m[i-1][j]== key:
      
        m[i-1][j]= cont
        conta += 1
        m,conta = revisar(m,i-1,j,key,cont,conta)
        
    if m[i][j-1] == key:
       
        m[i][j-1]= cont
        conta += 1
        m,conta = revisar(m,i,j-1,key,cont,conta)
        
    if m[i][j+1] == key:
       
        m[i][j+1]= cont
        conta += 1
        m,conta = revisar(m,i,j+1,key,cont,conta)
        
    if m[i+1][j] == key:
        
       
        m[i+1][j]= cont
        conta += 1
        m,conta = revisar(m,i+1,j,key,cont,conta)
        
    return m,conta

def recorrer(m,key):
    cont = 0
    conta = 0
    temp = 0
    for i in range(1,len(m)):
        for j in range(1,len(m[i])):
            if temp < conta:
                temp = conta
            if m[i][j] == key:
                conta = 1
                m[i][j] = cont
                m,conta = revisar(m,i,j,key,cont,conta)
               
                if j == 1 and m[i][len(m[i])-2] == key: 
                    m[i][len(m[i])-2] = cont
                    conta += 1
                    m,conta = revisar(m,i,len(m[i])-2,key,cont,conta)
                cont += 1
    print(temp)
    return m
            

def main():
    x = list(map(int,stdin.readline().split()))
    while x != []:
        m = []
        m.append([None]*(x[1]+2))
        for i in range(x[0]):
            m.append([None]+(list(stdin.readline().strip()))+[None])
        m.append([None]*(x[1]+2))
        c = list(map(int,stdin.readline().split()))
        key = m[c[0]+1][c[1]+1]
        
        m[c[0]+1][c[1]+1] = None
        conta = 0
        revisar(m,c[0]+1,c[1]+1,key,None,conta)
        recorrer(m,key)
        
        e = stdin.readline()
        x = list(map(int,stdin.readline().split()))
main()
