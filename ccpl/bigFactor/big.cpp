#include<bits/stdc++.h>
#define MAXI 10000002


using namespace std;


double res[MAXI];

void precal(){
    for(int i = 1; i < MAXI; i++){
        res[i] = res[i-1];
        res[i] += log10(i);
        //printf("%f\n",res[i]);
    }

}


int main(){
    
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int cases,n;
    precal();
    scanf("%d",&cases);
    for(int c = 0; c < cases; c++){
        scanf("%d",&n);
        //printf("%f\n",res[n]);
        //int r = (int)floor(res[n]) + 1;
        printf("%d\n",(int)floor(res[n]) + 1);
    }

    return 0;
}