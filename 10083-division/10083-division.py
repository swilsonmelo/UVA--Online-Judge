from sys import stdin
import math
m = stdin.readline().strip().split()
while m:
    m[0] = int(m[0])
    m[1] = int(m[1])
    m[2] = int(m[2])
    if m[0] == 1 or m[1] < m[2] or m[1] % m[2] != 0 or (m[1]-m[2]) * math.log10(m[0]) > 100 :
        print("("+str(m[0])+"^"+str(m[1])+"-1)/("+str(m[0])+"^"+str(m[2])+"-1) is not an integer with less than 100 digits.")
    elif m[1] == m[2]:
        print("("+str(m[0])+"^"+str(m[1])+"-1)/("+str(m[0])+"^"+str(m[2])+"-1)",1)
    else:
        x = ((int(m[0])**int(m[1]))-1)//((int(m[0])**int(m[2]))-1)
        print("("+str(m[0])+"^"+str(m[1])+"-1)/("+str(m[0])+"^"+str(m[2])+"-1)",x)
    m = stdin.readline().strip().split()
