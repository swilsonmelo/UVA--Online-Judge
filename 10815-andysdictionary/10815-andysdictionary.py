
from sys import stdin
import re

m = str(stdin.readline().strip())
dic = {}
z = []
while len(m) != 0:
    s = re.findall('[a-zA-Z]+', m)
    for i in s:
        x = i.lower()
        if x not in dic:
            dic[x] = 1
            z.append(x)
        else:
            dic[x] += 1
    m = str(stdin.readline().strip())
    if len(m) == 0:
        m = str(stdin.readline().strip())


salida = {}
y = 0
for i in dic:
    if dic[i] > y:
        y = dic[i]
#print(z)
for i in z:
    if dic[i] == y:
        suma = 0
        for j in i:
            suma += ord(j)
        salida[suma] = i
for i in salida:
    print(salida[i],i)
