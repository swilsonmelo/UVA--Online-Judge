from sys import stdin
import re




def magicBox(string):
    n = len(string)
    srt = (n)**(0.5)

    if(srt*srt != n):
        return 0
    stack = []
    pos = 0
    limi = n//2
   
    for i in range(limi):
        pos += 1
        stack.append(string[i])
    #print(pos)
    if n%2 == 1:
        stack.append(string[pos])

    for i in range(pos,n):
        top = stack.pop()
        if top != string[i]:
            return 0
    return srt



        
def main():

    n = int(stdin.readline().strip())
    for i in range(n):
        m = stdin.readline().strip()
        s = "".join(re.findall('[a-zA-Z]+', m))
        res = magicBox(s)
        print("Case #"+str(i+1)+":")
        if(res):
            print(int(res))
        else:
            print("No magic :(")
    

main()
