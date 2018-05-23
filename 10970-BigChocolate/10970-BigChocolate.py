from sys import stdin

m = stdin.readline().strip().split()
while m :
    print(int(m[0])*int(m[1])-1)
    m = stdin.readline().strip().split()
