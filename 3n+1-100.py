from sys import stdin
dict1 = {}


def main():
    m = list(map(int,stdin.readline().split()))
    while m != [] :

        j = max(m)
        i = min(m)
        maxi = 0 
        for x in range(j,i-1,-1):
            maxi = max(maxi,recu(x))
        print(m[0],m[1],maxi)
        m = list(map(int,stdin.readline().split()))
def recu(j):
    if j in dict1:
        return dict1[j]
    elif j == 1:
        return 1
    elif j % 2 != 0:
        
        dict1[3*j+1] = recu(3*j+1) 
        return dict1[3*j+1] + 1
    else:
        
        dict1[j//2] = recu(j//2) 
        return dict1[j//2] + 1


main()
