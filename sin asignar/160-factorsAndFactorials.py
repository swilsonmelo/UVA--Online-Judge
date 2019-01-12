from sys import stdin

fact = [1]*101
for i in range(1,101):
    fact[i] = fact[i-1]*i


seive = [1] *200
seive[0] = seive[1] = 0
facts = []
for i in range(2,200):
    if seive[i]:
        for j in range(i*i,200,i):
            seive[j] = 0
        facts.append(i)
#print(fact)

def main():
    n = int(stdin.readline().strip())
    while n != 0:
        r = fact[n]
        salida1 = []
        salida2 = []
        for i in range(100):
            num = facts[i]
            if r % num == 0:
                cont = 0
                while r % num == 0:
                    cont += 1
                    r //= num
                #print(cont)
                cont = str(cont)
                if len(salida1) < 15:
                    salida1.append(" "*(2-len(cont)) + cont)
                else:
                    salida2.append(" "*(2-len(cont)) + cont)
            if r == 1:
                break
        n = str(n)
        print(" "*(3-len(n))+n+"! = "+" ".join(salida1))
        if salida2:
            print(" "*(7)+" ".join(salida2))
        
        n = int(stdin.readline().strip())
    
main()
