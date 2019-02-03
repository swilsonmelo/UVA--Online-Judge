from sys import stdin

cnt = 100

def recu(a):
    global cnt
    
    temp = [x for  x in a]
    for i in range(11):
        if( a[i] == 'o' and a[i+1] == 'o'):
            if( i+2 < 12 and a[i+2] == '-'):
                a[i+2] = 'o'
                a[i] = '-'
                a[i+1] = '-'
                #print("".join(a),"1",i)
                recu(a)
                a = [x for x in temp]
            if( i - 1 >= 0 and a[i-1] == '-' ):
                #print("".join(a),"2.0",i)
                a[i-1] = 'o'
                a[i] = '-'
                a[i+1] = '-'
                #print("".join(a),"2",i)
                recu(a)
                a = [x for x in temp]
    res = 0
    #print(a)
    for i in a:
        if( i == 'o' ):
           res += 1
    if res < cnt:
        #print(a)
        cnt = res

def main():
    global cnt
    cases = int(stdin.readline().strip())
    for i in range(cases):
        cnt = 100
        a = stdin.readline().strip()
        a = [x for x in a]
        #print(a)
        recu(a)
        
        print(cnt)


main()
