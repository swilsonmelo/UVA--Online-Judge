from sys import stdin


def main():
    ini = [int(x) for x in stdin.readline().strip().split()]
    while ini:
        n,m = ini
        pos = [0]*(n*m +1)
        puzzle = [0]
        pasos = 0
        for i in range(1,n+1):
            fila = [int(x)for x in stdin.readline().strip().split()]
            for j in range(m):
                pos[fila[j]] = ((i-1)*m)+j + 1
            puzzle.append(fila)
        #print(puzzle)
        #print(pos)
        for i in range(1,(n*m)+1):
            #print(puzzle[i],i)
            if(puzzle[i] != i):
                pos2 = pos[i]
                pos[i] = i
                temp1 = puzzle[i]
                puzzle[i] = i
                pos[temp1] = pos2
                puzzle[pos2] = temp1
                pasos += 1
        if( pasos%2 == 0 ):
            
            print("Y",pasos)
        else:
            
            print("N",pasos)				
        ini = [int(x) for x in stdin.readline().strip().split()]



main()
