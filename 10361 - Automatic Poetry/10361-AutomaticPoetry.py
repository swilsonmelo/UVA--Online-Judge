from sys import stdin
import re

def main():

    n = int(stdin.readline().strip())
    for i in range(n):
        m = stdin.readline().strip().split()
        s = re.findall('[a-zA-Z]+', m)
        print(s)
        m = stdin.readline().strip()

main()
