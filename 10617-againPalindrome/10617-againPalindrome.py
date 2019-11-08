from sys import stdin

m = ""
dp = [[]]

def recu(i,j):
    if( i > j ): return 0
    if( i == j ): return 1
    res = dp[i][j]
    if(res != -1): return res
    res = recu(i+1,j) + recu(i,j-1)
    if(m[i] == m[j]):
        res += 1
        dp[i][j] = res
    else:
        res -= recu(i+1,j-1)
        dp[i][j] = res
    return res


def main():
    global dp, m
    cases = int(stdin.readline().strip())
    for c in range(cases):
        m = stdin.readline().strip()
        dp = [[ -1 for j in range(len(m))] for i in range(len(m))]
        print(recu(0,len(m)-1))
        
main()