from sys import stdin
dict = {}
def main():
    p = list(stdin.readline().split())
    while p != []:
        dict[p[1]] = p[0]
        p = list(stdin.readline().split())

    m = str(stdin.readline().strip())
    while m != "":
        if m in dict:
            print(dict[m])
        else:
            print("eh")
        m = str(stdin.readline().strip())


main()
            

    
