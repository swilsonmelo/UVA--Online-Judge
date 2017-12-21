from sys import stdin

def busqueda(dic,n):
    r = 0
    re = 1
    for i in dic :
        if r < dic[i]:
            r = dic[i]
            re = 1
        elif r == dic[i] and r != 1:
            re += 1
    if r*re == 1:
        print(n)
    else:
        print(re*r)
            
        


def main():
    n = int(stdin.readline())
    while n != 0:
        dic = {}
        for i in range(n):
            m = list(map(str,stdin.readline().split()))
            m.sort()
            if " ".join(m) not in dic:
                dic [" ".join(m)] = 1
            else:
                dic[" ".join(m)] += 1
        busqueda(dic,n)
        n = int(stdin.readline())

main()
        
            
