from sys import stdin


def getMatrixMult(mat1,mat2,mod):
    n = len(mat1)
    m = len(mat2[0])
    res = [[0 for j in range(m)] for i in range(n)]
    #print("mat1",len(mat1),len(mat1[0]))
    #print("mat2",len(mat2),len(mat2[0]))
    for i in range(n):
        for j in range(m):
            for k in range(len(mat1[0])):   
                #print(n,m,len(mat1[0]),i,j,k)
                res[i][j]  = (res[i][j]+mat1[i][k]*mat2[k][j])%mod
    return res


def getModExp(mat,p,mod):
    n = len(mat)
    m = len(mat[0])
    cont = 0
    res = [[0 for j in range(m)] for i in range(n)]
    
    while p > 0:
        #print(len(res),len(res[0]))
        #print("  ",len(mat),len(mat[0]))
        if(p%2 == 1):
            if(cont == 0):
                res = mat
            else:
                res = getMatrixMult(mat,res,mod)
            cont += 1
        p = p >> 1
        mat = getMatrixMult(mat,mat,mod)
    return res
    

def main():
    ini = [int(x) for x in stdin.readline().strip().split()]
    while ini:
        n,m = ini
        T = [[1,1],[1,0]]
        F = [[1],[1]]
        m = 2**m
        
        if n == 0:
            print(0)
        elif(n == 1 or n == 2):
            print(1)
        else:
            T = getModExp(T,n-2,m)
            F = getMatrixMult(T,F,m)
            print(F[0][0])
      
        ini = [int(x) for x in stdin.readline().strip().split()]
    

main()
