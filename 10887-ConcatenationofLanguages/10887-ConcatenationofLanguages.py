from sys import stdin


def main():
    cases = int(stdin.readline().strip())
    for ca in range(cases):
        n,m = [int(x) for x  in stdin.readline().strip().split()]
        s1 = set([])
        s2 = set([])
        setRes = set([])
        for i in range(n):
            x = stdin.readline().strip()
            s1.add(x)
        for i in range(m):
            x = stdin.readline().strip()
            s2.add(x)
        s1 = list(s1)
        s2 = list(s2)
        for i in range(len(s1)):
            for j in range(len(s2)):
                setRes.add(s1[i]+s2[j])
        print("Case",str(ca+1)+":",len(setRes))

main()
