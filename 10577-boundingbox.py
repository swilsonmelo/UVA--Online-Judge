import math
from sys import stdin

"""
formulas
Radio
R =(ab*bc*ca)/(4*area(ab,bc,ca))
semiperimetro
SP = (0.5*p)
perimetro
p = (ab+bc+ca)
Area
A = sqrt(s*(s-ab)*(s-bc)*(s-ca))
varicentro
varicentrox = (x1+x2+x3)/3
varicentroy = (y1+y2+y3)/3

t0 = artan((y1-y0)/(x1-x0))
(ti=t0+i/n*2*PI)
Pxi=cx+R*cos(ti); Pyi=cy+R*sin(ti)


De los puntos, tomar Pxmin, Pxmax, Pymin, Pymax  Área Mínima
OJO: n=3 es un caso especial. 
De los puntos, tomar Pxmin, Pxmax, Pymin, Pymax  Área Mínima
OJO: n=3 es un caso especial. 

"""
def circle(x1,y1,x2,y2,x3,y3):
    a = x1 - x2
    b = y1 - y2
    c = a*((x1+x2)/2) + b*((y1+y2)/2)
    d = x2 - x3
    e = y2 - y3
    f = d*((x2+x3)/2) + e*((y2+y3)/2)
    dd = a*e - b*d
    dx = c*e - b*f
    dy = a*f - d*c
    x0 = dx/dd
    y0 = dy/dd
    return x0,y0

def main():
    n = int(stdin.readline())
    conta = 1
    while n!= 0:
        x1,y1 = [float(x) for x in stdin.readline().strip().split()]
        x2,y2 = [float(x) for x in stdin.readline().strip().split()]
        x3,y3 = [float(x) for x in stdin.readline().strip().split()]
        x0,y0 = circle(x1,y1,x2,y2,x3,y3)
        theta = (2*math.pi/n)
        left = down = 10**30
        right = up = -(10**30)
        sintheta = math.sin(theta);
        costheta = math.cos(theta)
        prevx = x1
        prevy = y1
        for i in range(n):
            vx = prevx - x0
            vy = prevy - y0
            nextx = x0 + vx*costheta - vy*sintheta
            nexty = y0 + vx*sintheta + vy*costheta
            left = min(left, nextx)
            right = max(right, nextx)
            down = min(down, nexty)
            up = max(up, nexty)
            prevx = nextx
            prevy = nexty
        print("Polygon "+str(conta)+": "+"%.3f"%((right-left)*(up-down)))
        n = int(stdin.readline())
        conta += 1
        
main()
