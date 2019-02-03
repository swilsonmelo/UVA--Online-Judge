from sys import stdin


def recu(cad,n,ans,pos):
    #print(ans,len(ans),n,n==len(ans))
    if n == len(ans):
        #print("kha")
        print("".join(ans))
        return
    if pos >= len(cad):
        return
    c = cad[pos]
    ans += [c]
    recu(cad,n,ans,pos+1)
    ans.pop()
    for i in range(pos+1,len(cad)):
        if cad[i] == c:
            continue
        c = cad[i]
        ans += [c]
        recu(cad,n,ans,i+1)
        ans.pop()


def main():
    m = stdin.readline().strip().split()
    while m:
        s = [x for x in m[0]]
        n = m[1]
        s.sort()
        
        recu(s,int(n),[],0)
        
        m = stdin.readline().strip().split()

main()
