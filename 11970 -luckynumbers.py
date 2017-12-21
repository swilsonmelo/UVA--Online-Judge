from sys import stdin

cuadrados= [0]
for i in range(1,int(10**(9/2))+1):
    cuadrados.append(i**2)
    
def main():
    n = int(stdin.readline())
    for i in range(n):
        salida = []
        x = int(stdin.readline())
        for j in cuadrados[1:int(x**0.5)+1]:
            r = x-j
            
            if r**2 % (x -r) == 0:
                salida.append(r)
        salida.sort()
        m = list(map(str,salida))
        print("Case",str(i+1)+":"," ".join(m))
main()
