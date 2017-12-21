from sys import stdin

def solve(dif,rita,teo):
    x = 1
    y = 0
    a = 0
    b = 0
    while  a + b != rita + teo:
        
        if x >= 4:
            a+=x
        if x-y > dif:
            y += 1
            if y >= 3:
                 b += y
        x += 1
        #print(rita-a)
    print(rita-a)

def main():
    dif = stdin.readline().strip()
    while dif:
        dif = int(dif)
        rita = int(stdin.readline().strip())
        teo = int(stdin.readline().strip())
        solve(dif,rita,teo)
        #print(dif,rita,teo)
        dif = stdin.readline().strip()
main()
