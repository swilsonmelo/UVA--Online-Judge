from sys import stdin

def lfs(m,i,j):
    suma = 0    
    if m[i-1][j-1] == "*":
        suma = suma + 1
    if m[i-1][j] == "*":
        suma = suma + 1
    if m[i-1][j+1] == "*":
        suma = suma + 1
    if m[i][j-1] == "*":
        suma = suma + 1
    if m[i][j+1] == "*":
        suma = suma + 1
    if m[i+1][j-1] == "*":
        suma = suma + 1
    if m[i+1][j] == "*":
        suma = suma + 1
    if m[i+1][j+1] == "*":
        suma = suma + 1
    return suma
    

def floorfill(m):
    for  i in range(1,len(m)-1):
        for j in range(1,len(m[i])-1):
            if m[i][j] == ".":
                m[i][j] = lfs(m,i,j)



    for i in range(1,len(m)-1):
        m[i] = list(map(str,m[i]))
        print("".join(m[i][1:-1]))

def main():
    m = list(map(int,stdin.readline().split()))
    caso = 1
    while m != [0,0]:
        z = []
        z.append(["N"]*(m[1]+2))
        for i in range(m[0]):
            z.append(["N"]+list(stdin.readline().strip())+["N"])
        z.append(["N"]*(m[1]+2))
        print("Field #"+str(caso)+":")
        floorfill(z)
        caso += 1
        m = list(map(int,stdin.readline().split()))
        if m != [0,0]:
            print()
        
    
main()
