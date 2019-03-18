#include <bits/stdc++.h>
#define MAXI 1122

using namespace std;
typedef long long ll;
int isPrime[MAXI];
vector<int> primes;

ll dp[190][MAXI][15];

void seive(){
    for(int i = 0; i < MAXI; i++) isPrime[i] = 1;
    isPrime[0] = 0;
    isPrime[1] = 0;
    for(int i = 2; i < MAXI; i++){
        if(isPrime[i]){
            for(ll j = i*i; j < MAXI; j += i)isPrime[j] = 0;
            primes.push_back(i);
        }
    }
    //for(int i = 0; i < 11; i++) printf("%d ",primes[i]);
    //puts("");
    //printf("%d\n",primes.size());

}


ll solve(int posPrime, int n, int k){
    if( k == 0 ){
        if( n == 0 ) return 1;
        else return 0;
    }
    if(posPrime >= primes.size()) return 0;
    ll res = dp[posPrime][n][k];
    if( res != -1 ) return res;

    ll take = 0, dontTake = 0;
    if( n >= primes[posPrime] ) take = solve(posPrime+1,n-primes[posPrime],k-1);
    dontTake = solve(posPrime+1,n,k);
    res = take + dontTake;
    dp[posPrime][n][k] = res;
    return res;

}


int main(){
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    seive();
    memset(dp,-1,sizeof dp);
    int n,k;
    scanf("%d %d",&n,&k);
    while(n != 0 && k!=0){
        ll res = solve(0,n,k);
        printf("%lld\n",res);
        scanf("%d %d",&n,&k);
    }
    

    return 0;
}