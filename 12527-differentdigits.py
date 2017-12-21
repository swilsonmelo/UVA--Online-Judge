from sys import stdin

vec = []
cont = 0
for i in range(5005):
    if len(set(list(str(i)))) == len(str(i)):
        cont += 1
    vec.append(cont)
n = 2786
print(vec[n])
n = stdin.readline().strip().split()
while n :
    print(vec[int(n[1])]+1-vec[int(n[0])])
    n = stdin.readline().strip().split()

