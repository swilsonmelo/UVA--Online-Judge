#include <bits/stdc++.h>
#define MAXI 1000002

using namespace std;
typedef long long ll;

int isPrime[MAXI];
vector<int> primes;

void seive(){
    for(int i = 0; i < MAXI; i++)isPrime[i] = 1;
    isPrime[0] = isPrime[1] = 0;
    for(ll i = 0; i < MAXI; i++){
        if(isPrime[i]){
            primes.push_back(i);
            for(ll j = i*i; j < MAXI; j+= i)isPrime[j] = 0;
        }
    }

}

ll res[MAXI];

void precalc(){
    res[0] = res[1] = 0;
    for(int i = 2; i < MAXI; i++){
        res[i] = res[i-1];
        ll n = i;
        int pfi = 0, pf = primes[pfi];
        ll ans = 0;
        while( pf * pf <= n){
            while( n % pf == 0 ){
                ans++;
                n /= pf;
            }
            pfi++;
            pf = primes[pfi];
        }
        if( n != 1) ans++;
        res[i] += ans;
    }   

}


int main(){
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    seive();
    precalc();
    ll n;
    while(scanf("%lld", &n) == 1){
        printf("%lld\n",res[n]);

    }
    return 0;
}