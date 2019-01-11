from sys import stdin

def kadane(A):
    """
    ALgoitmo de kadane, progrmación dinámica
    """
    resL = resR = -1
    maxSum = currL = currR = currSum = 0
    for i in range(len(A)):
        if currSum < 0:
            currL,currR, currSum = i, i + 1, A[i]
        else:
            currR, currSum = i + 1, currSum + A[i]
        if (maxSum < currSum) or (maxSum == currSum and currR - currL > resR - resL):
            resL, resR, maxSum = currL, currR, currSum

    return resL,resR, maxSum
            
    
def main():
    cases = int(stdin.readline().strip())
    for i in range(cases):
        A = []
        n = int(stdin.readline().strip())
        for j in range(n-1):
            A.append(int(stdin.readline().strip()))
        resL, resR, maxSum = kadane(A)
        if maxSum > 0:
            
            print("The nicest part of route",i+1,"is between stops",resL + 1,"and",resR + 1)
        
        else:
            print("Route",i+1,"has no nice parts")
main()
