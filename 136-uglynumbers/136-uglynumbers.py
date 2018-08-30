
pos2 = 0
pos3 = 0
pos5 = 0

vec = [0]*(1500)
vec[0] = 1
#print(vec)
for i in range(1,1500):
    vec[i] = min(2*vec[pos2],3*vec[pos3],5*vec[pos5])
    #print(vec)
    if vec[i] == 2*vec[pos2]:
        pos2 += 1
    if vec[i] == 3*vec[pos3]:
        pos3 += 1
    if vec[i] == 5*vec[pos5]:
        pos5 += 1
    
    #print(pos2,pos3,pos5,pos7)
#print(vec)
print("The 1500'th ugly number is", str(vec[-1])+".")

print("The 1500'th ugly number is 859963392.")
