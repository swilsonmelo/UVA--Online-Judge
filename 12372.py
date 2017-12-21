from sys import stdin

def main():
    n = int(stdin.readline())
    for i in range(n):
        m = list(map(int,stdin.readline().split()))
        t = True
        for j in range(len(m)):
            if m[j] <= 20:
                t = True
            else:
                t= False
                break
        if t :
            print("Case "+str(i+1)+": good" )
        else:
            print("Case "+str(i+1)+": bad" )
main()
