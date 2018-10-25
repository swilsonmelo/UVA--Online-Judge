from sys import stdin



def main():
    n = int(stdin.readline().strip())
    for i in range(n):
        m = stdin.readline().strip()
        try:
            r = eval(m)
            print(r)
        except:
            print("ERROR")




main()    
