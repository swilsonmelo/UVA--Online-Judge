from sys import stdin

def main():
    m = list(map(int,stdin.readline().split()))
    t = set()
    ele = 0
    pare = 0
    inten = 0
    if m == [-1]:
        print(0)
        return
    while  m != []:
        x = False
        y = False
        if m[0] not in t:
            ele += 1
            x = True
        if m[1] not in t:
            ele += 1
            y = True
        
        pare += 1
        if ele == pare:
            inten += 1
            pare -= 1
        else:
            if not x and not y :
                inten += 1
                pare -=1

            if x :
                t.add(m[0])
            if y :
                t.add(m[1])
            
            
        m = list(map(int,stdin.readline().split()))
        if m[0] == -1:
            print(inten)
            t = set()
            ele = 0
            pare = 0
            inten = 0
            m = list(map(int,stdin.readline().split()))
            m = list(map(int,stdin.readline().split()))
            
        
main()
