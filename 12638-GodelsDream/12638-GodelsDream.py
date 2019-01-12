from sys import stdin


def main():
    global arr,res
    arr = list(stdin.readline().strip())
    while arr:
        res = 0
        cont = 0
        for pos in range(len(arr)):
            #print(cont,arr[pos],res)
            if arr[pos] == '0':
                if cont == 1 or cont == 0:
                    res += 1
                    cont = 0
                else: cont -= 1
            elif arr[pos] == '1':
                
                if cont == 0: cont = 2
                else: cont += 1
            else:
                if cont == 1 or cont == 0:
                    res += 1
                    cont = 0
                else: cont -= 1
        if(cont == 0): print(res)
        else :print(0)
        arr = list(stdin.readline().strip())


main()
