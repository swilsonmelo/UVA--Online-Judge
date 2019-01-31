from sys import stdin



def main():
    a = stdin.readline().strip()
    while a:
        
        k=0
        c=0
        lenCad = len(a);
        for j in range(lenCad):
            if(a[j]==a[lenCad-j-1]):
                k += 1
           

        for i in range(lenCad):
            if((a[i]=='A' and a[lenCad-i-1]=='A')or(a[i]=='E' and a[lenCad-i-1]=='3')or(a[i]=='3' and a[lenCad-i-1]=='E')or
               (a[i]=='H' and a[lenCad-i-1]=='H')or(a[i]=='I' and a[lenCad-i-1]=='I')or(a[i]=='J' and a[lenCad-i-1]=='L')or
               (a[i]=='L' and a[lenCad-i-1]=='J')or(a[i]=='M' and a[lenCad-i-1]=='M')or(a[i]=='O' and a[lenCad-i-1]=='O')or
               (a[i]=='2' and a[lenCad-i-1]=='S')or(a[i]=='T' and a[lenCad-i-1]=='T')or(a[i]=='U' and a[lenCad-i-1]=='U')or
               (a[i]=='V' and a[lenCad-i-1]=='V')or(a[i]=='W' and a[lenCad-i-1]=='W')or(a[i]=='X' and a[lenCad-i-1]=='X')or
               (a[i]=='Y' and a[lenCad-i-1]=='Y')or(a[i]=='Z' and a[lenCad-i-1]=='5')or(a[i]=='5' and a[lenCad-i-1]=='Z')or
               (a[i]=='1' and a[lenCad-i-1]=='1')or(a[i]=='S' and a[lenCad-i-1]=='2')or(a[i]=='8' and a[lenCad-i-1]=='8')):
                c += 1
        
        if(k==lenCad and lenCad==c):
            print(a,"-- is a mirrored palindrome.")
        elif(k==lenCad and lenCad!=c):
            print(a,"-- is a regular palindrome.")
        elif(k!=lenCad and lenCad==c):
            print(a,"-- is a mirrored string.")
        elif(k!=lenCad and lenCad!=c):
            print(a,"-- is not a palindrome.")
        print()
        a = stdin.readline().strip()
main()
