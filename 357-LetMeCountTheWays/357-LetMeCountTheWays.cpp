#include <bits/stdc++.h>
#define Maxi 30002

using namespace std;

long long ways[Maxi];
int coins[] = {5,10,25,50};

void precalc(){
    for(int i = 0; i < Maxi; i++) ways[i] = 1;

    for(int i  = 0; i < 4; i++){
        for(int j = 0; j < Maxi; j++){
            //printf("%d %d\n",j,coins[i]);
            if(coins[i]<= j){
                ways[j] += ways[j-coins[i]];
            }
        }
    }
    //for(int i = 0; i < 11; i++)printf("%d ",ways[i]);
    //puts("");
}


int main(){
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    precalc();
    int n;
    while(scanf("%d",&n) ==  1){
        if(ways[n]==1) printf("There is only 1 way to produce %d cents change.\n",n);
        else printf("There are %lld ways to produce %d cents change.\n",ways[n],n);

        //printf("%d %d\n",n,ways[n]);
    }
    
    return 0;
}
