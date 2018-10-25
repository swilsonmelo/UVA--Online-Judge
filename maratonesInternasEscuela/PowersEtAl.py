from sys import stdin
"""
Dados m y n halla el ultimo numero distinto de 0
de m**n
2 2 = 4
2 5 = 2
2341423412 321423412342314124324234213421341324321 = 2
1232334445 13124123123123123123123123530930900480984530 = 5

"""
def main():
    m = stdin.readline().strip().split()
    while m != ["0","0"]:
        ans = [[0],[1],[6,2,4,8],[1,3,9,7],[6,4],[5],[6],[1,7,9,3],[6,8,4,2],[1,9]]
        #The order of the loop, for the convenience of the index calculation, the last loop of each number is moved to the first
        mod = [1,1,4,4,2,1,1,4,4,2 ]
        #se refiere al tamaño de cada una de las sublistas de ans
        sm,sn = m
        if sn[0] == "0":
            print(1)
        else:
            len_M = len(sm)
            len_N = len(sn)
            m = int(sm[-1])
            n = int(sn)
            n = n%mod[m]
            #también se puede definir n así
            """
            for i in range(len_n):
                n = n*10 + int(sn[i])
                n %= mod[m]
            """
            ##
            print(ans[m][n])
            
        m = stdin.readline().strip().split()
main()
