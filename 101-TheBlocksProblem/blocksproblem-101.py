from sys import stdin
def volver(a,i):
    global y
    while y[i][-1] != a:
        y[y[i][-1]].append(y[i].pop())
        
    
def move_onto(a,b):
    global y
    for i in range(len(y)):
        if a in y[i]:
            if b in y[i]:
                return
            elif y[i][-1] == a:
                y[i].pop()
                break
            else:
                volver(a,i)
                y[i].pop()
                break
            
    for i in range(len(y)):
        if b in y[i]:
            if y[i][-1] == b:
                y[i].append(a)
                break
            else:
                volver(b,i)
                y[i].append(a)
                break

def move_over(a,b):
    global y
    for i in range(len(y)):
        if a in y[i]:
            if b in y[i]:
                return
            if y[i][-1] == a:
                y[i].pop()
                break
            else:
                volver(a,i)
                y[i].pop()
                break
            
    for i in range(len(y)):
        if b in y[i]:
            y[i].append(a)
            break


def pile_onto(a,b):
    global y
    x = []
    for i in range(len(y)):
        if a in y[i]:
            if b in y[i]:
                return
            for j in range(len(y[i])):
                if y[i][-1] == a:
                    x.append(y[i].pop())
                    break
                else:
                    x.append(y[i].pop())
            break
    x = x[::-1]
    #print(x)
    
      
    for i in range(len(y)):
        if b in y[i]:
            volver(b,i)
            y[i] = y[i] + x
            break



def pile_over(a,b):
    global y
    x = []
    for i in range(len(y)):
        if a in y[i]:
            if b in y[i]:
                return
            for j in range(len(y[i])):
                if y[i][-1] == a:
                    x.append(y[i].pop())
                    break
                else:
                    x.append(y[i].pop())
            break
    x = x[::-1]
    #print(x)
    
      
    for i in range(len(y)):
        if b in y[i]:
            y[i] = y[i] + x
            break




def main():
    global y
    n = int(stdin.readline())
    y = []
    for i in range(n):
        x = []
        x.append(i)
        y.append(x)
    m = list(stdin.readline().split())
    while m[0]!= "quit":
        if m[0] == "move":
            if m[2] == "onto":

                move_onto(int(m[1]),int(m[3]))
            else:

                move_over(int(m[1]),int(m[3]))
        else:
            if m[2] == "onto":

                pile_onto(int(m[1]),int(m[3]))
            else:

                pile_over(int(m[1]),int(m[3]))
        
        
        m = list(stdin.readline().split())

    for i in range(len(y)):
        if len(y[i]) == 0 :
            print(str(i)+":")
        else:
            y[i] = list(map(str,y[i]))
            print(str(i)+":"," ".join(y[i]))

main()
