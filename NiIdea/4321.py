import sys
def func():
    n = list(map(int,sys.stdin.readline().split()))
    for i in range(n[1]):
        drag = list(map(int,sys.stdin.readline().split()))
        if n[0] > drag[0]:
            n[0] += drag[1]
        else:
            
            return False
    return True

def main():
    if func():
        print("YES")
    else:
        print("NO")
main()

