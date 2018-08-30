from sys import stdin

def caminos(m,i,j,cont):
    if m[i-1][j-1] == "1" :
        m[i-1][j-1] = cont
        m = caminos(m,i-1,j-1,cont)
    if m[i-1][j] == "1" :
        m[i-1][j] = cont
        m = caminos(m,i-1,j,cont)
    if m[i-1][j+1] == "1" :
        m[i-1][j+1] = cont
        m = caminos(m,i-1,j+1,cont)
    
    if m[i][j-1] == "1" :
        m[i][j-1] = cont
        m = caminos(m,i,j-1,cont)

    if m[i][j+1] == "1" :
        m[i][j+1] = cont
        m = caminos(m,i,j+1,cont)

    if m[i+1][j+1] == "1" :
        m[i+1][j+1] = cont
        m = caminos(m,i+1,j+1,cont)
        
    if m[i+1][j] == "1" :
        m[i+1][j] = cont
        m = caminos(m,i+1,j,cont)
        
    if m[i+1][j-1] == "1" :
        m[i+1][j-1] = cont
        m = caminos(m,i+1,j-1,cont)

    return m
    
        

def recorrer(m,n):
    cont = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if m[i][j] == "1":
                m[i][j] = cont
                m = caminos(m,i,j,cont)
                cont +=1
    
    return cont
            

def main():
    conta = 1
    n = stdin.readline().strip()
    while n != "" :

        n = int(n)
        m = []
        m.append(["0"]*(n+2))
        for i in range(n):
            
            m.append(["0"]+list(stdin.readline().strip())+["0"])
        m.append(["0"]*(n+2))
        cont = recorrer(m,n)
        print("Image number "+str(conta)+" contains "+str(cont)+" war eagles.")
        n = stdin.readline().strip()
        conta += 1
main()
