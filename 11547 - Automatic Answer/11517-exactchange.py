from sys import stdin
INF = 10005
Nmax = 10005

def main():
    casos = int(stdin.readline())
    for i in range(casos):
        valor = int(stdin.readline())
        deno = []
        mone = int(stdin.readline())
        for i in range(mone):
            deno.append(int(stdin.readline()))
        salida  = solve(valor, deno)
        print(salida[0],salida[1])

    
def solve(total, value):
    M = len(value)
    memo = [INF] * Nmax
    memo[0] = 0
    for v in value:
        for j in range(v, Nmax):
                memo[j] = min(memo[j], memo[j - v] + 1)
    pos = total
    while pos < Nmax  and memo[pos] == INF:
        pos += 1
    return [pos,memo[pos]]

main()


