from sys import stdin


def func(m,i,j):
    global dict
    if str(i)+","+str(j) in dict :
        return dict[str(i)+","+str(j)]

    if j==i+1:
        return abs(m[i]-m[j])
    elif i==j+1:
        return 0
    elif j-i+1>2:
        if m[i+1] >= m[j]:
            izq = m[i]- m[i+1]+func(m,i+2,j)
        elif m[i+1]<m[j]:
            izq = m[i]-m[j]+func(m,i+1,j-1)
        if m[i]>= m[j-1]:
            der = m[j]-m[i]+func(m,i+1,j-1)
        elif m[i]< m[j-1]:
            der =  m[j]-m[j-1]+func(m,i,j-2)
        dict[str(i)+","+str(j)] = max(izq,der)
        return dict[str(i)+","+str(j)]
        
def main():
    global dict
    cont = 1
    m=[int(x) for x in stdin.readline().strip().split()]
    while m[0]!=0:
        dict = {}
        
        x = m.pop(0)
        y = func(m,0,x-1)
        print("In game",str(cont)+", the greedy strategy might lose by as many as",y,"points.")
        m=[int(x) for x in stdin.readline().strip().split()]
        cont += 1
main()
