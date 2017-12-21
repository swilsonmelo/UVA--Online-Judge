from sys import stdin


def backtrack(total, step):
    if total > maxTotal:
        return
    if step == N:
        if  total >= best[1]:
            best[0] = list(path)
            best[1] = sum(path)
        return

    backtrack(total, step + 1)
    path.append(A[step])
    backtrack(total + A[step], step + 1)
    path.pop()

A = list(map(int,stdin.readline().split()))
while A:
    path = []
    best = [0, 0]
    maxTotal, N = A[0], A[1]
    del A[0:2]
    backtrack(0, 0)
    print (" ".join(map(str,best[0])), "sum:"+str(sum(best[0])))
    A= list(map(int,stdin.readline().split()))
