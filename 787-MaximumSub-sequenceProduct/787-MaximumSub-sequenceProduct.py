from sys import stdin

"""

Esto funicona, solo si es resultado es positivo.


def kadaneModif(arr):
    maxEndingHere = 1
    minEndingHere = 1
    maxSoFar = 1
    for i in range(len(arr)-1):
        if(arr[i] > 0):
            maxEndingHere *= arr[i]
            minEndingHere = min(minEndingHere * arr[i],1)
        elif(arr[i] == 0):
            maxEndingHere = 1
            minEndingHere = 1
        else:
            temp = maxEndingHere
            maxEndingHere = max(minEndingHere* arr[i], 1)
            minEndingHer = temp * arr[i]
        if(maxSoFar < maxEndingHere):
            maxSoFar = maxEndingHere

    return maxSoFar


"""
def main():

    m = [int(x) for x in stdin.readline().strip().split()]
    while m:
        #print(m)
        maxPro = -999999
        for i in range(len(m)-1):
            currPro = 1
            for j in range(i,len(m)-1):
                currPro *= m[j]
                #print(currPro,maxPro)
                maxPro = max(currPro, maxPro)
        print(maxPro)
            
        m = [int(x) for x in stdin.readline().strip().split()]




main()
