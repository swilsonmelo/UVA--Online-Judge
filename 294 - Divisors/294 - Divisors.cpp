#include <bits/stdc++.h>
#define Maxi 32000
using namespace std;

int seive[Maxi];
vector<long long>primes;

void criba(){
    for(int i = 0; i < Maxi; i++) seive[i] = 1;
    seive[0] = 0;
    seive[1] = 0;

    for(long long i = 2; i < Maxi; i++){
        if(seive[i]){
            primes.push_back(i);
            for(long long j = i*i; j < Maxi; j += i)seive[j] = 0;
        }
    }
    /*
    for(int i = 0; i < 15; i++) printf("%lld ",primes[i]);
    puts("");
    */
}


long long numDiv(long long n){
    long long pfIndex = 0, pf = primes[pfIndex], ans = 1;
    while( pf * pf <= n){
        long long power = 0;
        while( n % pf == 0 ){
            n /= pf;
            power++;
        }
        ans *= (power + 1);
        pfIndex++;
        pf = primes[pfIndex];
    }
    if( n != 1 ) ans *= 2;
    return ans;

}

int main(){
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    criba();
    int cases;
    long long a,b;
    scanf("%d",&cases);
    for(int c = 0; c < cases; c++){
        scanf("%lld %lld",&a,&b);
        long long maxDiv = 1LL;
        long long maxi = 1LL;
        for(long long i = a; i <= b; i++ ){
            long long res = numDiv(i);
            if(res > maxi){
                maxi = res;
                maxDiv = i;
            }
        }
        printf("Between %lld and %lld, %lld has a maximum of %lld divisors.\n",a,b,maxDiv,maxi);

    }
    return 0;
}
