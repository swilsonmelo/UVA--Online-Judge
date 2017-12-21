from sys import stdin

def func(n):
    d1 = n % 100
    n //= 100
    d2 = n % 10
    n //= 10
    d3 = n % 100
    n //= 100
    d4 = n % 100
    n //= 100
    if n > 100:
        result = func(n)
        result.append('kuti')
    else:
        result = []
    if d4:
        result.append(str(d4))
        result.append('lakh')
    if d3:
        result.append(str(d3))
        result.append('hajar')
    if d2:
        result.append(str(d2))
        result.append('shata')
    if d1:
        result.append(str(d1))
    return result


def main():
    cont = 1
    n = stdin.readline().strip()
    while n :
        print(" "*(4-len(str(cont)))+str(cont)+"."," ".join(func(int(n))))
        cont += 1
        n = stdin.readline().strip()

main()
