from sys import stdin

dp = [[-1 for j in range(210)] for i in range(210)]

def solve(pos, left):
    global n,m
    #print(pos,left)
    r = dp[pos][left]
    if(  r != -1 ): return r
    res = 0
    t = 0
    for i in range(pos,n):
        if( m[i] <= left ):
            #print(i)
            t = m[i] + solve(i+1, left-m[i])
            
            if ( res < t):
                res = t 
    dp[pos][left] = res
    #print("res",pos,left,dp[pos][left])
    return res


def main():

    global n,m
    cases = int(stdin.readline().strip())

    for c in range(cases):
        m = [int(x) for x in stdin.readline().strip().split()]
        n = len(m)
        suma = sum(m)
        if( suma % 2 != 0):
            print("NO")
        else:
            suma //= 2
            for i in range(210):
                for j in range(210):
                    dp[i][j] = -1
            res = solve(0,suma) 
            #print(suma)
            if( res == suma):
                print("YES")
            else:
                print("NO")

main()