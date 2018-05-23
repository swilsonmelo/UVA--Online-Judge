from sys import stdin

def warshall(m):
    suma = 0
    cont = 0
    for k in range(len(m)):
        for i in range(len(m)):
            for j in range(len(m)):
                m[i][j] = min(m[i][j],m[i][k]+m[k][j])
    
    for i in range(len(m)):
        for j in range(len(m)):
            if i != j :
                suma +=m[i][j]
                cont += 1
    return suma,cont

def main():
    caso = 1
    m = [int(x) for x in stdin.readline().strip().split()]
    while m != [0,0]:
        dic1 = {}
        dic2={}
        x = 0
        for i in range(0,len(m)-2,2):
            if m[i] not in dic1:
                dic1[m[i]] = x
                dic2[x] = m[i]
                x += 1
            if m[i+1] not in dic1:
                dic1[m[i+1]] = x
                dic2[x] = m[i+1]
                x += 1
        mat = [[2**31-1 for i in range(len(dic1))] for j in range(len(dic1))]
        for i in range(0,len(m)-2,2):
            mat[dic1[m[i]]][dic1[m[i+1]]] = 1
        suma,cont= warshall(mat)
        print("Case "+str(caso)+": average length between pages = %.3f clicks"%(suma/cont))
        m = [int(x) for x in stdin.readline().strip().split()]
        caso += 1
main()

    
