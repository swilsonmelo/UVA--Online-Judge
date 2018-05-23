from sys import stdin


def func(a,b):
    m = []
    for i in range(len(b)+1):
        col = []
        for j in range(len(a)+1):
            col.append(0)
        m.append(col)
    
    for i in range(len(a)+1):
        
        m[0][i] = i
  
    for i in range(len(b)+1):
        
        m[i][0] = i
   

    for i in range(1,len(b)+1):
        for j in range(1,len(a)+1):
            
            if b[i-1] == a[j-1]:
                y = 0
            else:
                y= 1
            m[i][j] = min(m[i-1][j]+1,m[i-1][j-1]+y,m[i][j-1]+1)

    print(m[-1][-1])
def main():
    n = int(stdin.readline())
    for i in range(n):
        a = str(stdin.readline().strip())
        b = str(stdin.readline().strip())
        if len(a) == 0 or len(b) == 0:
            print(max(len(a),len(b)))
        elif a == b:
            print(0)
        else:
            func(a,b)


main()
