from sys import stdin
top = 5003
vec = [0,1]
for i in range(2,top):
    vec.append(vec[i-1]+vec[i-2])
"""
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    elif n in dic:
        return dic[n]
    else:
        dic[n] = fibonacci(n-1)+fibonacci(n-2)
        return dic[n]
"""
def main():
    global dic
    dic = {}
    n = stdin.readline().strip()
    while n:
        print("The Fibonacci number for "+n+" is",vec[int(n)])
        n = stdin.readline().strip()

main()
