from sys import stdin


def recu(i,j,n):
    global dic
    if i >= j:
        s1 = 0
        if i == n:
            s1 += 0
        elif i < n:
            max1 = 0
            for k in range(i+1,n+1):
                if str(k)+"-1" not in dic :
                    recu(k,1,n)
                if str(k)+"-"+str(j) not in dic:
                    recu(k,j,n)
                max1 = max(max1,dic[str(k)+"-1"]+dic[str(k)+"-"+str(j)])
            s1 += max1
        s2 = 0
        if j > 1:
            max2 = 0
            for k in range(1,j):
                if str(i)+"-"+str(k) not in dic:
                    recu(i,k,n)
                if str(n)+"-"+str(k) not in dic :
                    recu(n,k,n)
                max2 = max(max2,dic[str(i)+"-"+str(k)]+dic[str(n)+"-"+str(k)])
            s2 += max2
        elif j == 1:
            s2 += 0
        dic[str(i)+"-"+str(j)] = s1 + s2
        return 0
    elif i < j :
        max3 = 0
        for k in range(i,j):
            if str(i)+"-"+str(k) not in dic:
                recu(i,k,n)
            if str(k+1)+"-"+str(j) not in dic:
                recu(k+1,j,n)
            max3 = max(max3,dic[str(i)+"-"+str(k)]+dic[str(k+1)+"-"+str(j)])
        dic[str(i)+"-"+str(j)] = max3
        return 0
                
            
                

def main():
    global dic
    x = list(map(int,stdin.readline().split()))
    while x !=[]:
        dic = {}
        n=x[0]        
        dic[str(n)+"-1"] = x[1]
        recu(1,n,n)
        print(dic["1-"+str(n)])
        print(dic)
        x = list(map(int,stdin.readline().split()))
    
main()
    
