from sys import stdin



def main():
    m = [int(x) for x in stdin.readline().strip().split()]
    while m:
        r1 = (m[0]*(m[0]-1)*m[1])//2
        r2 = m[3]
        diff = r1 - r2
        res = diff // m[2]
        if( res <= 0 or res >= m[0] ):
            print(m[0])
        else:
            print(res)
        m = [int(x) for x in stdin.readline().strip().split()]
main()