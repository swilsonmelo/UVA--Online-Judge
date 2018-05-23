from sys import stdin


def main():
    while True:
        n = int(stdin.readline())
        if n == 0:
            break
        m =  int(stdin.readline())
        graph = [[0 for y in range(n)] for x in range(n)]
        color = [-1]*n

        for i in range(m):
            a,b = list(map(int,stdin.readline().split()))
            graph[a][b] = 1
            graph[b][a] = 1

        q = [0]
        color[0] = 0
        t = True

        while q:
            u = q.pop(0)
            for v in range(n):
                if not graph[u][v]:
                    continue
                if color[v] == -1:
                    color[v] = color[u] + 1
                    q.append(v)

                elif color[u] == color[v] :
                    t = False
                    break
            if not t :
                break

        if t:
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE.")
main()
