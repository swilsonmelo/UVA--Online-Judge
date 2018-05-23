from sys import stdin


cod = {}
cod["A"] = 2
cod["B"] = 2
cod["C"] = 2
cod["D"] = 3
cod["E"] = 3
cod["F"] = 3
cod["G"] = 4
cod["H"] = 4
cod["I"] = 4
cod["J"] = 5
cod["K"] = 5
cod["L"] = 5
cod["M"] = 6
cod["N"] = 6
cod["O"] = 6
cod["P"] = 7
cod["R"] = 7
cod["S"] = 7
cod["T"] = 8
cod["U"] = 8
cod["V"] = 8
cod["W"] = 9
cod["X"] = 9
cod["Y"] = 9
cod["0"] = 0
cod["1"] = 1
cod["2"] = 2
cod["3"] = 3
cod["4"] = 4
cod["5"] = 5
cod["6"] = 6
cod["7"] = 7
cod["8"] = 8
cod["9"] = 9

def salidas():
    salida = {}
    z = []
    for i in dic:
        if dic[i] > 1:
            z.append(i)
    z.sort()
    
    if z:
        for i in range(len(z)):
            print(z[i][:3]+"-"+z[i][3:],dic[z[i]])
    else:
        print("No duplicates.")
            


def main():
    global dic
    casos = int(stdin.readline())
    for i in range(casos):
        print("Test Case",str(i+1)+":")
        dic = {}
        tele = int(stdin.readline())
        for j in range(tele):
            m = list(map(str,stdin.readline().strip()))
            l = []
            for x in m:
                if x in cod:
                    l.append(str(cod[x]))
            l = "".join(l)
            if l in dic:
                dic[l] += 1
            else:
                dic[l] = 1
        salidas()
        print()
        
                    
            
main()
