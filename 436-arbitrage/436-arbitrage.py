from sys import stdin

def warshall(m):

    for k in range(len(m)):
        for i in range(len(m)):
            for j in range(len(m)):
                m[i][j] = max(m[i][j],m[i][k]*m[k][j])

    return m

def main():
    caso = 1
    n = int(stdin.readline())
    while n != 0 :
        dic = {}
        m = [[0 for i in range(n)]for j in range(n)]
        for i in range(n):
            dic[str(stdin.readline().strip())] = i
        
        arc = int(stdin.readline())
        for i in range(arc):
            x,y,z = [v for v in stdin.readline().strip().split()]
            m[dic[x]][dic[z]] = float(y)
        m = warshall(m)
        t = True
        for i in range(n):
            if m[i][i] > 1:
                print("Case "+str(caso)+": Yes")
                t = False
                break
        if t :
            print("Case "+str(caso)+": No")
            
            
        blank = stdin.readline()
        n = int(stdin.readline())
        caso += 1
main()
