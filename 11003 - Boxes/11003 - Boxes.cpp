#include <bits/stdc++.h>
#define MAXI 1005

using namespace std;

int weight[MAXI];
int load[MAXI];
int boxes;
int maxNumberWithLoadLeft[MAXI][3005];


int canHold( int currentBox, int loadLeft ){
    if( currentBox == boxes) return 0;
    int num = maxNumberWithLoadLeft[currentBox][loadLeft];
    if( num != -1 ) return num;
    num = canHold(currentBox + 1,loadLeft);// No lo tomo
    if( loadLeft >= weight[currentBox] ){
            /* tomo la caja actual y mi nueva resistencia sera la mínima entre la que tenía menos la que hay ahora
                y la resistencia de la caja actual
            */
            num = max(num, 1 + canHold(
                                       currentBox + 1, min( loadLeft - weight[currentBox],load[currentBox] )
                                        )
                      );
    }
    maxNumberWithLoadLeft[currentBox][loadLeft] = num;
    return num;


}

int solve(){
    int res = 0;
    for(int i = 0; i < boxes; i++){
        res = max(res,1 + canHold(i + 1 ,load[i]) );
    }
    return res;

}


int main(){
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    scanf("%d",&boxes);
    while( boxes ){
        int maxLoad = 0;
        for(int i = 0; i < boxes; i++){
            scanf("%d %d",&weight[i],&load[i]);
            maxLoad = max(maxLoad,load[i]);
        }

        for(int i = 0; i < boxes; i++){
            for(int j = 0; j <= maxLoad; j++){
                maxNumberWithLoadLeft[i][j] = -1;
            }
        }

        int res = solve();
        printf("%d\n",res);
        scanf("%d",&boxes);
    }


    return 0;
}

