from sys import stdin

x = [-1,-1,-1, 0,0,1,1,1]
y = [-1, 0, 1,-1,1,-1,0,1]

def count(i,j,mat):
    mines = 0
    for k in range(8):
        a = i+x[k]
        b = j+y[k]
        if( 0 <= a and a < len(mat)) and (0 <= b and b < len(mat[0])):
            if mat[a][b] == "*":
                mines += 1

    return mines

def solve(mat):

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == ".":
                mat[i][j] = count(i,j,mat)
    return mat
    

def main():
    n,m = [int(x) for x in stdin.readline().strip().split()]
    case = 1
    while n and m:
        matriz = []
        for i in range(n):
            matriz.append(list(stdin.readline().strip()))

        mat = solve(matriz)
        print("Field #"+str(case)+":")
        for i in mat:
            print("".join(list(map(str,i))))
        n,m = [int(x) for x in stdin.readline().strip().split()]
        if n != 0 and m!= 0:
            print()
        case += 1

main()
