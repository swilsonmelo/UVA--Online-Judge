import sys
def funx():
    n = int(sys.stdin.readline())
    while n != 0:
        
        mat = []
        contf = 0
        for i in range(n):
            
            l1 = list(map(int,sys.stdin.readline().split()))
            if sum(l1) % 2 != 0:
                x = i
                contf += 1
            mat.append(l1)
        contc = 0
        for j in range(n):
            columna = []
            
            for i in range(n):
                columna.append(mat[i][j])
            if sum(columna) % 2 != 0:
                y = j
                contc += 1
                
        if contf == contc == 0 :
            w = True
            print("OK")
        elif contf == contc == 1:
            
            print("Change bit ("+str(x+1)+","+str(y+1)+")")
            
            
        else:
            w = False
            print("Corrupt")
        
        
        
        n = int(sys.stdin.readline())
funx()
