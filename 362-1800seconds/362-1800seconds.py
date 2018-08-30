from sys import stdin
import math
def main():
    x = int(stdin.readline())
    conta = 1
    while x:
        print("Output for data set",str(conta)+",",str(x),"bytes:")
        conta+=1
        suma = 0
        arch = 0
        while x >0:
            a = int(stdin.readline())
            arch += 1
            if a > 0 :
                suma += a
                x -= a
            if arch % 5 == 0:
                if suma > 0:
                    y = int(math.ceil((x*5)/suma))
                    print("   Time remaining:",y,"seconds")
                else:
                    print("   Time remaining: stalled")
                suma = 0
        print("Total time:",arch,"seconds")
        print()
        x = int(stdin.readline())
main()
