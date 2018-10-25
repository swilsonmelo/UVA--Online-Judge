from sys import stdin


def perimeter(ab,bc,ca):
    return ab+bc+ca

def semiPerimeter(ab,bc,ca):
    return 0.5*perimeter(ab,bc,ca)

def area(ab,bc,ca):
    s = semiPerimeter(ab,bc,ca)
    return (s*(s-ab)*(s-bc)*(s-ca))**0.5

def rInCircle(ab,bc,ca):
    return area(ab,bc,ca)/(0.5*perimeter(ab,bc,ca))
    
    


def main():
    m = [float(x) for x in stdin.readline().strip().split()]

    while m:
        ab,bc,ca = m
        #print(m)
        
        if 0 in m:
            r = 0
        else:
            r = (rInCircle(ab,bc,ca))
        print("The radius of the round table is: %.3f"%r)
        #print("%.3f"%(rInCircle(ab,bc,ca)))
        m = [float(x) for x in stdin.readline().strip().split()]

main()
