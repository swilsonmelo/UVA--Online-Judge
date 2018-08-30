from sys import stdin


def busqueda(m):
    global dic , z
    for i in m:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
            z.append(i)
dic = {}
z = []

m = list(map(int,stdin.readline().split()))
while m != []:
    busqueda(m)
    m = list(map(int,stdin.readline().split()))

for i in z:
    print(i,dic[i])
