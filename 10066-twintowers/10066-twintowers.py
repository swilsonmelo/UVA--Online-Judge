from sys import stdin


def llenar(m,n,mat,s,t):
    for i in range(1,m+1):
        for j in range(1,n+1):
            
            if s[i-1] == t[j-1]:
                mat[i][j] = mat[i-1][j-1] + 1
            elif mat[i-1][j] >= mat[i][j-1]:
                mat[i][j] = mat[i-1][j]
            else:
                mat[i][j] = mat[i][j-1]
    """
    for i in range(m):
            print(mat[i])
    """
    print("Number of Tiles :",mat[-1][-1])
            
            

def main():
    casos = 1
    x = list(map(int,stdin.readline().split()))
    while x != [0,0]:
        s = list(map(int,stdin.readline().split()))
        t = list(map(int,stdin.readline().split()))
        mat = []
        for i in range(x[0]+1):
            f = []
            for j in range(x[1]+1):
                f.append(0)
            mat.append(f)
        print("Twin Towers #"+str(casos))
        llenar(x[0],x[1],mat,s,t)
        print()
        casos += 1
        x = list(map(int,stdin.readline().split()))
main()
