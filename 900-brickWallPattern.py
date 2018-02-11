from sys import stdin

vec = [0]*55
vec[0] = vec[1] = 1
for i in range(2,55):
    vec[i] = vec[i-1] + vec[i-2]

def main():
    x = int(stdin.readline().strip())
    while x != 0:
        print(vec[x])
        x = int(stdin.readline().strip())

main()
