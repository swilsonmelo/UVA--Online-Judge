from sys import stdin

"""
BOUND = 1000005
vec = [0]*BOUND
vec[0] = vec[1] = 1
primes = []
for i in range(2,BOUND):
    if(not vec[i]):
        primes.append(i)
        for j in range(i*i,BOUND,i):
            vec[j] = 1

#print(primes)

circulares = []
for i in range(len(primes)):

    y = primes[i]
    x = str(y)
    isCirc = 1
    for j in range(len(x)):
        x = x[1:] + x[0]
        if( vec[int(x)]):
            isCirc = 0
            break
    if isCirc: circulares.append(y)


print(circulares)
"""
arr = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, 1931, 3119, 3779, 7793, 7937, 9311, 9377, 11939, 19391, 19937, 37199, 39119, 71993, 91193, 93719, 93911, 99371, 193939, 199933, 319993, 331999, 391939, 393919, 919393, 933199, 939193, 939391, 993319, 999331]

def main():
    n = [int(x) for x in stdin.readline().strip().split()]
    while n!=[-1]:
        cont = 0
        for i in range(len(arr)):
            if arr[i] > n[1]: break
            elif(arr[i] >= n[0] and arr[i] <= n[1]): cont +=1

        if(cont == 0): print("No Circular Primes.")
        elif(cont == 1): print("1 Circular Prime.")
        else: print(cont,"Circular Primes.")
        n = [int(x) for x in stdin.readline().strip().split()]
main()
