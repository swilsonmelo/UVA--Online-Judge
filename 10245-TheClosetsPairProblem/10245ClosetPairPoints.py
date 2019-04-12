from sys import stdin
"""
La distancia más corta entre n puntos
Dividir y conquistar complejidad O(nLog(n))
También esta en uva como el ejercicio 10245
"""
def distance(p1,p2):
    x = (p1[0]-p2[0])*(p1[0]-p2[0])
    y = (p1[1]-p2[1])*(p1[1]-p2[1])
    return x+y

def merge(puntos,low,mid,high,minLeft,minRight):
    dis1 = min(minLeft,minRight)
    #print(mid)
    line = (puntos[mid][0]+puntos[mid+1][0])//2#linea en la mitad de los puntos
    
    minTotal = dis1
    for i in range(mid+1,high+1):
        if puntos[i][0] >= line+dis1: #reviso que no pase de la linea + mi distancia mínima
            break
        for j in range(mid,low-1,-1):
            if puntos[i][0] <= line-dis1: #reviso que no pase de la linea - mi distancia mínima
                break
            dis2 = distance(puntos[i],puntos[j])
            minTotal = min(minTotal,dis2)
    return minTotal
            
def divide(puntos,low,high):
    if low >= high:
        return float("inf")
    mid = (low+high)//2
    minLeft = divide(puntos,low,mid)
    minRight = divide(puntos,mid+1,high)
    return merge(puntos,low,mid,high,minLeft,minRight)

def main():
    nums = int(stdin.readline().strip())
    while nums != 0:
        puntos = []
        for i in range(nums):
            puntos.append([float(x) for x in stdin.readline().strip().split()])
        puntos.sort()
        #print(puntos)
        dis = divide(puntos,0,nums-1)**0.5
        if dis >= 10000:
            print("INFINITY")
        else:
            print("%.4f"%(dis))
        
        nums = int(stdin.readline().strip())
main()
