#include <bits/stdc++.h>
#define loop(i,a,b) for(i=a;i<b;i++)
using namespace std;
int main(){
    int cases,R,C,id,i;
    scanf("%d",&cases);
    loop(id,0,cases){
        int l=0,num,m=0;
        scanf("%d %d",&R,&C);
        loop(i,0,R*C){
            scanf("%d",&num);
            if (i%2==0)l+=(-num);
            else m+=(-num);
        }
        if (l==m){
             printf("Case #%d: YES\n",id+1);
        }
        else {
                printf("Case #%d: NO\n",id+1);
        }
        puts("");
    }
    return 0;
}
