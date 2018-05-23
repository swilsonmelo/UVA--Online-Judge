from sys import stdin
import math
def main():
    m = list(map(int,stdin.readline().split()))
    while m != [0,0]:
        print((math.floor(math.sqrt(m[1])) - math.ceil(math.sqrt(m[0])) + 1))
        m = list(map(int,stdin.readline().split()))
main()
