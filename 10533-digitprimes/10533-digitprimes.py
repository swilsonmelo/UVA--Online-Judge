from sys import stdin
top = 1000002
vec = [True]*top
vec[0] = vec[1] = False
salida = [0]*top
cont = 0
for i in range(top):
    
    if vec[i] :
        x = sum(list(map(int,str(i))))
        if vec[x] :
            cont += 1
        for j in range(i+i,top,i):
            vec[j] = False
    salida[i] = cont

def main():
    n = int(stdin.readline())
    for i in range(n):
        x,y = [int(x) for x in stdin.readline().split()]
        print(salida[y]-salida[x-1])

main()
