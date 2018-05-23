from  sys import stdin


def salida(m,maxi):
    global dic
    sal = []
    for i in range(10):
        if dic[m[i]] == maxi:
            sal.append(m[i])
    for i in range(len(sal)):
        print(sal[i])
            

def main():
    global dic
    n = int(stdin.readline())
    for i in range(n):
        dic = {}
        z = []
        maxi = 0
        for j in range(10):
            m = list(stdin.readline().split())
            if int(m[1]) > maxi:
                maxi = int(m[1])
            z.append(m[0])
            dic[m[0]] = int(m[1])
        print("Case #"+str(i+1)+":")
        salida(z,maxi)

main()
                
