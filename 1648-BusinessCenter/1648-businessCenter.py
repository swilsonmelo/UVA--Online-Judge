from sys import stdin



def main():

    entrada = [int(x) for x in stdin.readline().strip().split()]
    while entrada:
        n,m = entrada
        mini = 2**31-1
        for i in range(m):
            u,d = [int(x) for x in stdin.readline().strip().split()]
            low = 0
            high = n
            while low <= high:
                mid = (low+high)//2
                lv = u * mid - (n - mid) * d
                if lv > 0:
                    high = mid - 1
                    mini = min(mini,lv)
                else:
                    low = mid + 1
        print(mini)
        #print(n,m)
        entrada = [int(x) for x in stdin.readline().strip().split()]
        

main()
