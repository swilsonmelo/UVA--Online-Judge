import sys
def recibir():
    dicc1=[]
    pareja=list(sys.stdin.readline().split())
    while pareja != []:
        dicc1.append(pareja)
        pareja = list(sys.stdin.readline().split())
    dicc2 = []
    for i in range(len(dicc1)):
        dicc2.append(dicc1[i][0])
        dicc2.append(dicc1[i][1])
        
    palabras = []
    sig = list(sys.stdin.readline().split())
    while sig != []:
        palabras.append(sig[0])
        sig = list(sys.stdin.readline().split())


    for i in range(len(palabras)):
        if palabras[i] in dicc2 :
            
            if dicc2.index(palabras[i]) % 2 !=0:
                print(dicc2[dicc2.index(palabras[i])-1])
            else:
                print("eh")
        else:
            print("eh")
recibir()
