#include<bits/stdc++.h>
#define MaxiV 50005
#define MaxiC 105

using namespace std;

int dp[MaxiC][MaxiV];
int coins[MaxiC];
int n;
int sum;

int solve(int pos,int value){
    if(pos == n) return abs(value - (sum - value));
    int res = dp[pos][value];
    if(res != -1) return res;

    res = min(solve(pos+1,value),solve(pos+1,value + coins[pos]));
    dp[pos][value] = res;
    return res;
}

int main(){
    int cases;
    scanf("%d",&cases);
    for(int c = 0; c < cases; c++){
        memset(dp, -1, sizeof dp);
        scanf("%d",&n);
        sum = 0;
        for(int i = 0; i < n; i++){
            scanf("%d",&coins[i]);
            sum += coins[i];
        }
        int res = solve(0,0);
        printf("%d\n",res);
    }

    return 0;
}