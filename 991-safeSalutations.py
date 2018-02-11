from sys import stdin
import math


vec = [0] *11
for i in range(1,11):
    vec[i] = (math.factorial(2*i)/(math.factorial(i)*math.factorial(i)*(i+1)))
def main():

    x = stdin.readline().strip()
    while x:
        print(int(vec[int(x)]))
        stdin.readline()
        x = stdin.readline().strip()
        if(x):print()

main()
