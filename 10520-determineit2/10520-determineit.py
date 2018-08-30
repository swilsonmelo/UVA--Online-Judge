from sys import stdin


m=[]
for i in range(21):
    f=[]
    for j in range(21):
        f.append(0)
    m.append(f)

def main():
    x = list(map(int,stdin.readline().split()))
    while x != []:
        n = x[0]-1
        val = x[1]
        m[n][0] = val
        
        for i in range(n+1,-1,-1):
            for j in range(n):
                if i == n and j ==0:
                    continue
                if i >= j:
                    x1 = 0
                    x2 = 0
                    for y in range(i+1,n+1):
                        x1 = max(x1, m[y][1]+m[y][j])
                    for y in range(j):
                        x2 = max(x1, m[i][y]+m[n][y])
                    m[i][j] = x1 + x2
                else:
                    z = 0
                    for y in range(i,j):
                        z = max(z, m[i][y]+m[y+1][j])
        for i in range(20):
            print(m[i])
        print(m[0][n])
        x = list(map(int,stdin.readline().split()))
main()            
        
