import sys
def main():
    n = list(sys.stdin.readline().split())
    s = []
    for i in range(int(n[0])):
        info = list(sys.stdin.readline().split())
        s.append(info[0])
    l1=[]
    cont = 0
    for i in range(len(s)):
        if s[cont] == s[i] and not s[cont] in l1:
            l1.append(s[cont])
            

        cont += 1
    l1.sort()
    frecu = []
    for i in range(len(l1)):
        cont2 = 0
        for j in range(len(s)):
            if l1[i] == s[j]:
                cont2 +=1
        frecu.append(cont2)
    for i in range(len(l1)):
        print(l1[i],frecu[i])
    
main()
