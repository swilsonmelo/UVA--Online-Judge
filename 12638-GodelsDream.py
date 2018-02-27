from sys import stdin
res = 0
arr = []
def solve(pos,cont,cantG):
    global arr,res
    if pos>= len(arr):
        #print(cont)
        if cont == 0:
            res = cantG
        return 1
        
    if arr[pos] == '0':
        if cont == 1 or cont == 0: return solve(pos+1,0,cantG+1)
        else: return solve(pos+1,cont-1,cantG)
    elif arr[pos] == '1':
        if cont == 0: return solve(pos+1,2,cantG)
        else: return solve(pos+1,cont+1,cantG)
    else:
        arr[pos] = '0'
        if(solve(pos,cont,cantG)): return 1
        arr[pos] = '1'
        if(solve(pos,cont,cantG)): return 1
        arr[pos] = '?'

    return 0
            
            

def main():
    global arr,res
    arr = list(stdin.readline().strip())
    while arr:
        res = 0
        solve(0,0,0)
        print(res)
        
        arr = list(stdin.readline().strip())


main()
