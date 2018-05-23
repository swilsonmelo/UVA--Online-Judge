from sys import stdin

dr = [0,0,1,-1]
dc = [1,-1,0,0]
dire = ["R", "L", "D", "U"]
INF = 2**31 - 1
found = -1
A = [[] for i in range(4) ]
Er = 0
Ec = 0
path = []

def H():
    h = 0
    for i in range(4):
        for j in range(4):
            if A[i][j] == 0:
                continue
            expect_r = ((A[i][j]-1) // 4)
            expect_C = ((A[i][j]-1) % 4)
            h += abs(expect_r - i) + abs(expect_C - j)
            #print("A[i][j]",A[i][j],"expect_r",expect_r,"expect_C",expect_C)
    #print("en H h",h)
    return h

def dfs(g, pdir, bound):
    global Er,Ec
    h = H()
    #print("h",h)
    f = g + h
    if( f > bound ): return f
    if( h == 0): return found
    mn = INF
    for i in range(4):
        if( i == (pdir ^ 1)):
            continue
        nr = Er + dr[i]
        nc = Ec + dc[i]
        if( nr < 0 or nr >= 4): continue
        if( nc < 0 or nc >= 4): continue
        path.append(dire[i])
        cop = A[nr][nc]
        A[nr][nc] = A[Er][Ec]
        A[Er][Ec] = cop
        cop = nr
        nr = Er
        Er = cop
        cop = nc
        nc = Ec
        Ec = cop
        t = dfs(g+1, i, bound)
        if( t == found ): return found
        if( t < mn ): mn = t
        cop = nr
        nr = Er
        Er = cop
        cop = nc
        nc = Ec
        Ec = cop
        cop = A[nr][nc]
        A[nr][nc] = A[Er][Ec]
        A[Er][Ec] = cop
        path.pop()
    return mn


def IDAstar():
    global Er,Ec,path
    bound = H()
    while( True ):
        #print("Bound",bound)
        t = dfs(0,-1, bound)
        #print("Er Ec t",Er,Ec,t)
        if( t == found ): return True
        if( t == INF ): return False
        if( t>= 50 ): return False
        bound = t

def solvable():
    global Er,Ec,path
    cnt = 0
    occur = [False] * 16
    for i in range(4):
        for j in range(4):
            if( A[i][j] == 0 ):
                Er = i
                Ec = j
            else:
                x = A[i][j]
                #print(" cnt",cnt,"Er",Er,"Ec",Ec,"X",x )
                cnt += occur[1:x].count(False)
                occur[x] = True
    #print("Er",Er,"Ec",Ec)
    return (cnt + (Er + 1))%2 == 0

def main():
    global Er,Ec,path
    cases = int(stdin.readline().strip())
    for ca in range(cases):
        for i in range(4):
            A[i] = [int(x) for x in stdin.readline().strip().split()]
        
        path = []
        #for i in A:
        #   print(i)
        #"""
        #x  = solvable()
        #y = IDAstar()
        #print(x,y,path)
        if( not solvable() or not IDAstar()):
            print("This puzzle is not solvable.")
        else:
            print("".join(path))
        #"""
main()

















