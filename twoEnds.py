from sys import stdin


def func(i,j):
    global dict,m
    if str(i)+","+str(j) in dict :
        return dict[str(i)+","+str(j)]
    if j==i+1:
        dict[str(i)+","+str(j)] = abs(m[i]-m[j])
        return dict[str(i)+","+str(j)]
    elif i==j+1:
        dict[str(i)+","+str(j)] = 0
        return dict[str(i)+","+str(j)]
    elif j-i+1>2:
        if m[i+1] >= m[j]:
            izq = m[i]- m[i+1]+func(i+2,j)
        elif m[i+1]<m[j]:
            izq = m[i]-m[j]+func(i+1,j-1)
        if m[i]>= m[j-1]:
            der = m[j]-m[i]+func(i+1,j-1)
        elif m[i]< m[j-1]:
            der =  m[j]-m[j-1]+func(i,j-2)
        dict[str(i)+","+str(j)] = max(izq,der)
        return dict[str(i)+","+str(j)]
        
def main():
    global dict,m
    cont = 1
    m=[int(x) for x in stdin.readline().strip().split()]
    while m[0]!=0:
        dict = {}
        x = m.pop(0)
        y = func(0,x-1)
        print("In game",str(cont)+", the greedy strategy might lose by as many as",y,"points.")
        m=[int(x) for x in stdin.readline().strip().split()]
        cont += 1
main()
