from sys import stdin
"""
prim = []
primos = ["True"] * 100000
primos[0] = primos[1] = False
for i in range(2,len(primos)):
    if primos[i]:
        for j in range(i,len(primos),i):
            primos[j] = False
        prim.append(int(i))


print(1)
vec = []
i = 1
while cont < 5842:
    maxi = 1
    t = True
    for j in prim:
        if i % j == 0:
            if j > maxi:
                maxi = j
        if maxi > 7:
            t = False
            break
    if t :
        vec.append(i)
    i += 1
            
print(i)
"""
pos2 = 0
pos3 = 0
pos5 = 0
pos7 = 0
vec = [0]*20
vec[0] = 1
#print(vec)
for i in range(1,20):
    vec[i] = min(2*vec[pos2],3*vec[pos3],5*vec[pos5],7*vec[pos7])
    #print(vec)
    if vec[i] == 2*vec[pos2]:
        pos2 += 1
    if vec[i] == 3*vec[pos3]:
        pos3 += 1
    if vec[i] == 5*vec[pos5]:
        pos5 += 1
    if vec[i] == 7*vec[pos7]:
        pos7 += 1
    #print(pos2,pos3,pos5,pos7)
#print(vec)

def main():
    n = int(stdin.readline())
    while n != 0:
        if n %10 == 1 and int((n/10)%10) != 1:
            x = "st"
        elif n %10 == 2 and int((n/10)%10) != 1:
            x = "nd"
        elif n %10 == 3 and int((n/10)%10) != 1:
            x = "rd"
        else:
            x = "th"
        print("The "+str(n)+x,"humble number is",str(vec[n-1])+".")
        n = int(stdin.readline())

main()

