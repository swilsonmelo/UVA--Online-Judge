from sys import stdin

def main():
    m = list(stdin.readline().strip())
    conta = 0
    cont = 0
    while m != []:
        for i in range(len(m)):
            
            if m[i] == '"':
                if cont == 0 :
                    cont += 1 
                    m[i] = "``"

                else: 
                    cont = 0
                    m[i] = "''"
     
        print("".join(m))
        conta += 1
        m = list(stdin.readline().strip())

main()
