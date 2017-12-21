from sys import stdin
def find(p):
    global pare
    if p == pare[p]:
        return p
    else:
        x = pare[p] = find(pare[p])
        return x
    
def main():
    global pare
    m = list(map(int,stdin.readline().split()))
    if m == [-1]:
        m = list(map(int,stdin.readline().split()))
        print(0)
        m = list(map(int,stdin.readline().split()))
        
        
    pare = {}
    for i in range(((10)**5)+3):
        pare[i] = i
    inten = 0
    while  m != []:
        if find(m[0])==find(m[1]):
            inten += 1
        else:
            pare[find(m[0])] = find(m[1])
        m = list(map(int,stdin.readline().split()))
        if m[0] == -1:
            print(inten)
            pare = {}
            for i in range(((10)**5)+3):
                pare[i] = i
            inten = 0
            m = list(map(int,stdin.readline().split()))
            m = list(map(int,stdin.readline().split()))
                   
main()
