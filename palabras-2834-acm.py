from sys import stdin
import re

def salidas(z):
    salida = {}
    y = 0
    for i in dic:
        if dic[i] > y:
            y = dic[i]
    for i in z:
        if dic[i] == y:
            suma = 0
            for j in i:
                suma += ord(j)
            salida[suma] = i
    print(y,"occurrences")
    print(salida)
    for i in salida:
        print(salida[i])
    
def main():
    global dic
    n = int(stdin.readline())
    blank = stdin.readline()
    for y in range(n):
        dic = {}
        z = []
        m = str(stdin.readline().strip())
        while m!="":
            s = re.findall('[a-zA-Z]+', m)
            for i in s:
                x = i.lower()
                if x not in dic:
                    dic[x] = 1
                    z.append(x)
                else:
                    dic[x] += 1
            m = str(stdin.readline().strip())
        
        salidas(z)
        if y != n-1:
            print()
            
main()
