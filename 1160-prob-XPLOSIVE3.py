from sys import stdin

def find(x):
    if padre[x] == x:
        return x
    else:
        padre[x] = find(padre[x])
        return padre[x]

paren = [(i) for i in range(1000700)]

while True:
    padre = paren.copy()
    lis = [int(x) for x in stdin.readline().split()]
    cont = 0
    if lis != []:
        while lis[0] != -1:
            x = lis[0]
            y = lis[1]
            if find(x) == find(y):
                cont += 1
            else:
                padre[find(x)] = find(y)
                
            lis = [int(x) for x in stdin.readline().split()]
    else:
        break
    print(cont)
    blan = stdin.readline()


            
