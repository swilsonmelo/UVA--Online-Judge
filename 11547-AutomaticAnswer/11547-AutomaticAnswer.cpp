#include <bits/stdc++.h>
using namespace std;


int main(){
    int cases,x;
    scanf("%d",&cases);
    while(cases--){
        scanf("%d",&x);
        x*= 567; x/= 9; x+= 7492;
        x*= 235; x/= 47; x-= 498;
        x/= 10; x%= 10;
        if( x < 0 ) x*= -1;
        printf("%d\n",x);
    }

    return 0;
}
