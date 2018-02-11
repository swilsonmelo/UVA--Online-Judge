from sys import stdin

fib = [0]*101
fib[1] = fib[0] = 1 
for i in range(2,101):
    fib[i] = fib[i-1] + fib[i-2]
    


def main():
    a = [ str(x) for x in stdin.readline().strip()]
   
    
    while a :
        b = [ str(x) for x in stdin.readline().strip()]
        a1 = '0b'+"".join(a)
        b1 = '0b'+"".join(b)
        if a1==b1:
            b1[::-1]
        x = int(a1,2)
        y = int(b1,2)
        r = bin(x+y)
        unosPeg = 0
        for i in range(2,len(r)):
            if unosPeg == 2: break
            if r[i] =='1': unosPeg +=1
            else: unosPeg = 0
        #print(unosPeg,r,int(r,2))
        if unosPeg == 2:
            #print(unosPeg)
            while unosPeg == 2:
                #print(bin(int(r,2)+1)[2:])
                r = bin(int(r,2)+1)
                unosPeg = 0
                #print(r)
                for i in range(2,len(r)):
                    if unosPeg == 2: break
                    if r[i] =='1': unosPeg +=1
                    else: unosPeg = 0
            
        print(r[2:])
        print()
        """
        for i in range(len(a)):
            print(fib[lim1])
            x += a[i]*fib[lim1]
            lim1 -= 1
        for i in range(len(b)):
            print(fib[lim2])
            y += b[i]*fib[lim2]
            lim2 -= 1"""
        #print(a1,int(a1,2),b1,int(b1,2))
        stdin.readline()
        a = [ str(x) for x in stdin.readline().strip()]
        
main()
